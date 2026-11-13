"""Fixtures for the Synapse ID notation in the staging YAML comments (scripts/staging_index.py)."""
import os, sys, textwrap, pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import staging_index as si

@pytest.mark.parametrize("text,ids", [
    ("syn70095506", ["syn70095506"]),
    ("syn78566204, syn78580438, syn78592024", ["syn78566204", "syn78580438", "syn78592024"]),
    ("syn726677{15..17}", ["syn72667715", "syn72667716", "syn72667717"]),
    ("syn7346269{3,5}", ["syn73462693", "syn73462695"]),
    ("syn754273{57,59..61,58}", ["syn75427357", "syn75427359", "syn75427360", "syn75427361", "syn75427358"]),
    ("syn7542733{08..10}", ["syn754273308", "syn754273309", "syn754273310"]),
])
def test_expand(text, ids):
    assert si.expand(text) == ids

@pytest.mark.parametrize("bad", ["syn12345{a..b}", "syn12345{1-3}", "syn12345{1..}"])
def test_expand_rejects_unknown_notation(bad):
    with pytest.raises(ValueError):
        si.expand(bad)

def test_parser_and_independent_check_agree(tmp_path):
    y = tmp_path / "s.yml"
    y.write_text(textwrap.dedent("""\
        top: #syn11111111
          export: #syn70095506
            batch{1..5}: #syn78566204, syn78580438, syn78592024, syn78609685, syn78624654
              - MiGA_eQTL.*.cis_results_db.export.rds
          fine_mapping: #syn75134502
            batch{1..10}: #syn754273{57,59..66,58}
              - X.*.rds
        """))
    tree = si.parse(str(y))
    def ids(n):
        out = set(n.get("ids", [])) | set(n.get("fileids", []))
        for c in n.get("children", []): out |= ids(c)
        return out
    assert ids(tree) == si.independent_ids(str(y))
    assert len(si.independent_ids(str(y))) == 1 + 1 + 5 + 1 + 10

def test_real_yaml_ids_all_parsed():
    repo = os.path.join(os.path.dirname(__file__), "..")
    y = os.path.join(repo, "data", "statfungen_synapse_staging_folder_structure.yml")
    tree = si.parse(y)
    def ids(n):
        out = set(n.get("ids", [])) | set(n.get("fileids", []))
        for c in n.get("children", []): out |= ids(c)
        return out
    assert ids(tree) == si.independent_ids(y)
