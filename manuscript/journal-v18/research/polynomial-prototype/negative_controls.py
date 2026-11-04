#!/usr/bin/env python3
"""Mutation controls in a new disposable tree; never edit source candidates."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

source = Path(__file__).with_name("check_polynomial_objects.py")
spec = importlib.util.spec_from_file_location("prototype_verifier", source)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def main():
    checker.need(len(sys.argv) == 3, "candidate and new mutation directory")
    original = checker.load(sys.argv[1])
    checker.verify(original)
    target = Path(sys.argv[2])
    target.mkdir(exist_ok=False)
    fixtures = []

    def mutate(name, fn):
        obj = copy.deepcopy(original)
        fn(obj)
        fixtures.append((name, json.dumps(obj, sort_keys=True).encode()))

    mutate("missing_case", lambda o: o["cases"].pop())
    mutate("duplicate_case", lambda o: o["cases"].__setitem__(1, o["cases"][0]))
    mutate("reordered_cases", lambda o: o["cases"].reverse())
    mutate("unknown_case", lambda o: o["cases"][0].update(id="conditional6"))
    mutate("scope_change", lambda o: o.update(scope="current_proof_ancestor"))
    mutate("extra_field", lambda o: o.update(accepted=True))
    mutate("wrong_variables", lambda o: o.update(variables=["a", "x"]))
    mutate("empty_polynomial", lambda o: o["cases"][0].update(quotient=[]))
    mutate("duplicate_monomial", lambda o: o["cases"][0]["quotient"].append([1, 0, "1"]))
    mutate("noncanonical_rational", lambda o: o["cases"][0]["quotient"][0].__setitem__(2, "4/2"))
    mutate("float_coefficient", lambda o: o["cases"][0]["quotient"][0].__setitem__(2, 2.0))
    mutate("negative_exponent", lambda o: o["cases"][0]["quotient"][0].__setitem__(0, -1))
    mutate("boolean_exponent", lambda o: o["cases"][0]["quotient"][0].__setitem__(0, False))
    for i in range(3):
        mutate("corrupt_conditional" + str(i + 3),
               lambda o, i=i: o["cases"][i]["quotient"][0].__setitem__(2, "17"))
    for i in (3, 4):
        for field in ("numerator", "derivative_numerator", "moment_difference"):
            mutate("corrupt_radial" + str(i + 1) + "_" + field,
                   lambda o, i=i, field=field: o["cases"][i][field][0].__setitem__(2, "17"))
    blob = json.dumps(original, sort_keys=True)
    fixtures.append(("duplicate_json_key", ('{"format":"duplicate",' + blob[1:]).encode()))
    rows = []
    for name, payload in fixtures:
        path = target / (name + ".json")
        path.write_bytes(payload)
        try:
            checker.verify(checker.load(path))
        except checker.Reject as exc:
            rows.append({"name": name, "rejected": True, "reason": str(exc),
                         "sha256": hashlib.sha256(payload).hexdigest()})
        else:
            raise RuntimeError("mutation accepted: " + name)
    print(json.dumps({"status": "PASS_NEGATIVE_CONTROLS", "controls": rows,
                      "count": len(rows), "current_manuscript_ancestor": False}, sort_keys=True))


if __name__ == "__main__":
    main()
