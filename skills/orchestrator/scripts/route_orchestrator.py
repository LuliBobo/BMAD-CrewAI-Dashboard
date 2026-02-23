#!/usr/bin/env python3
"""Deterministicke prve routovanie pre BMAD Orchestrator skill."""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from typing import Dict, List, Tuple


AGENT_RULES: List[Tuple[str, List[str]]] = [
    (
        "Orchestrator",
        [
            "orchestrator",
            "which agent",
            "workflow",
            "route this",
            "how do i",
            "ktory agent",
            "aky workflow",
            "nasmeruj to",
            "ako to mam urobit",
        ],
    ),
    (
        "Analyst",
        [
            "analyze",
            "analysis",
            "research problem",
            "discovery",
            "explore options",
            "analyza",
            "analyzuj",
            "prieskum problemu",
            "objavovanie",
            "preskumaj moznosti",
        ],
    ),
    (
        "Product Manager (PM)",
        [
            "prd",
            "product requirement",
            "user needs",
            "success criteria",
            "roadmap scope",
            "produktove poziadavky",
            "potreby pouzivatelov",
            "kriteria uspechu",
            "rozsah roadmapy",
        ],
    ),
    (
        "UX Designer",
        [
            "ux",
            "user flow",
            "wireframe",
            "interaction design",
            "usability",
            "pouzivatelsky tok",
            "interakcny navrh",
            "pouzitelnost",
        ],
    ),
    (
        "Architect",
        [
            "architecture",
            "adr",
            "scalability",
            "technical constraints",
            "system design",
            "architektura",
            "skalovatelnost",
            "technicke obmedzenia",
            "navrh systemu",
        ],
    ),
    (
        "Scrum Master (SM)",
        [
            "epic",
            "story",
            "sprint",
            "backlog",
            "iteration planning",
            "epika",
            "uzivatelsky pribeh",
            "planovanie sprintu",
            "sprava backlogu",
        ],
    ),
    (
        "Developer (Dev)",
        [
            "implement",
            "code",
            "feature",
            "bug fix",
            "build this",
            "implementuj",
            "napis kod",
            "funkcionalita",
            "oprava chyby",
            "postav toto",
        ],
    ),
    (
        "QA / Quinn",
        [
            "qa",
            "test automation",
            "test plan",
            "coverage",
            "regression test",
            "automatizacia testov",
            "testovaci plan",
            "pokrytie testov",
            "regresne testy",
        ],
    ),
    (
        "Code Reviewer",
        [
            "code review",
            "review this pr",
            "standards check",
            "review findings",
            "kontrola kodu",
            "skontroluj kod",
            "skontroluj pr",
            "kontrola standardov",
            "podla standardov",
            "zistenia z review",
        ],
    ),
    (
        "Refactorer",
        [
            "refactor",
            "cleanup code",
            "technical debt",
            "maintainability",
            "refaktoring",
            "vycisti kod",
            "technicky dlh",
            "udrzatelnost kodu",
        ],
    ),
    (
        "Release/DevOps Agent",
        [
            "deploy",
            "ci/cd",
            "pipeline",
            "release",
            "infrastructure",
            "nasadenie",
            "produkcia",
            "devops",
            "infra",
        ],
    ),
    (
        "Tech Writer / Documentarian",
        [
            "documentation",
            "docs",
            "changelog",
            "technical writing",
            "dokumentacia",
            "technicka dokumentacia",
            "release notes",
            "zmenovy log",
        ],
    ),
    (
        "Project Context Curator",
        [
            "project-context.md",
            "project context",
            "sync context",
            "projektovy kontext",
            "synchronizuj kontext",
            "aktualizuj project context",
        ],
    ),
    (
        "Retrospective Facilitator",
        [
            "retrospective",
            "lessons learned",
            "post-mortem",
            "retrospektiva",
            "retrospektivu",
            "zorganizuj retrospektivu",
            "ponaucenia",
            "post mortem",
        ],
    ),
    (
        "Researcher",
        [
            "market research",
            "deep research",
            "benchmark",
            "compare technologies",
            "trhovy vyskum",
            "hlbsi vyskum",
            "porovnaj technologie",
            "porovnanie technologii",
        ],
    ),
    (
        "Business Strategist",
        [
            "business goal",
            "go-to-market",
            "prioritization",
            "business case",
            "biznis ciel",
            "prioritizacia",
            "obchodna strategia",
            "business plan",
        ],
    ),
    (
        "Idea Coach / Brainstorming Coach",
        [
            "brainstorm",
            "idea generation",
            "new product ideas",
            "brainstorming",
            "generovanim napadov",
            "generovanie napadov",
            "napady na produkt",
        ],
    ),
    (
        "Quick-Spec Agent",
        [
            "quick spec",
            "small change spec",
            "concise spec",
            "rychla specifikacia",
            "kratku specifikaciu",
            "specifikaciu zmeny",
            "kratka specifikacia",
            "spec pre malu zmenu",
        ],
    ),
    (
        "Quick-Dev Agent",
        [
            "quick dev",
            "small change now",
            "ad-hoc implementation",
            "rychla implementacia",
            "ad hoc implementaciu",
            "ad hoc implementac",
            "sprav to hned",
            "ad hoc implementacia",
        ],
    ),
    (
        "Correct-Course Agent",
        [
            "change direction",
            "course correction",
            "replan sprint",
            "mid-sprint change",
            "korekciu smeru",
            "korekciu smeru pocas sprintu",
            "zmena smeru",
            "korekcia smeru",
            "preplanuj sprint",
            "zmena pocas sprintu",
        ],
    ),
    (
        "Support / Help Agent",
        [
            "/bmad-help",
            "bmad help",
            "help me choose",
            "bmad pomoc",
            "pomoz mi vybrat",
            "ako pokracovat",
        ],
    ),
]

AGENT_ALIASES_SK: Dict[str, str] = {
    "Orchestrator": "Koordinator",
    "Analyst": "Analytik",
    "Product Manager (PM)": "Produktovy Manazer (PM)",
    "UX Designer": "UX Dizajner",
    "Architect": "Architekt",
    "Scrum Master (SM)": "Scrum Master (SM)",
    "Developer (Dev)": "Vyvojar (Dev)",
    "QA / Quinn": "QA / Quinn",
    "Code Reviewer": "Kontrolor Kodu",
    "Refactorer": "Refaktorer",
    "Release/DevOps Agent": "Release/DevOps Agent",
    "Tech Writer / Documentarian": "Technicky Pisatel / Dokumentarista",
    "Project Context Curator": "Kurator Projektoveho Kontextu",
    "Retrospective Facilitator": "Facilitator Retrospektivy",
    "Researcher": "Vyskumnik",
    "Business Strategist": "Biznis Strateg",
    "Idea Coach / Brainstorming Coach": "Kouc Napadov / Brainstorming Kouc",
    "Quick-Spec Agent": "Quick-Spec Agent",
    "Quick-Dev Agent": "Quick-Dev Agent",
    "Correct-Course Agent": "Agent Korekcie Smeru",
    "Support / Help Agent": "Podpora / Help Agent",
}

DEFAULT_SUPPORTING: Dict[str, str] = {
    "Analyst": "Product Manager (PM)",
    "Product Manager (PM)": "Architect",
    "UX Designer": "Product Manager (PM)",
    "Architect": "Scrum Master (SM)",
    "Scrum Master (SM)": "Developer (Dev)",
    "Developer (Dev)": "QA / Quinn",
    "QA / Quinn": "Code Reviewer",
    "Code Reviewer": "Refactorer",
    "Refactorer": "Developer (Dev)",
    "Release/DevOps Agent": "Tech Writer / Documentarian",
    "Tech Writer / Documentarian": "Project Context Curator",
    "Project Context Curator": "Tech Writer / Documentarian",
    "Retrospective Facilitator": "Scrum Master (SM)",
    "Researcher": "Business Strategist",
    "Business Strategist": "Product Manager (PM)",
    "Idea Coach / Brainstorming Coach": "Analyst",
    "Quick-Spec Agent": "Quick-Dev Agent",
    "Quick-Dev Agent": "QA / Quinn",
    "Correct-Course Agent": "Scrum Master (SM)",
    "Support / Help Agent": "Orchestrator",
    "Orchestrator": "Analyst",
}


def normalize(text: str) -> str:
    stripped = "".join(
        ch for ch in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(ch) != "Mn"
    )
    return " ".join(stripped.strip().split())


def score_request(text: str) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    scores: Dict[str, int] = {}
    matched: Dict[str, List[str]] = {}

    for agent, keywords in AGENT_RULES:
        hits = [kw for kw in keywords if normalize(kw) in text]
        matched[agent] = hits
        scores[agent] = sum(2 if " " in kw else 1 for kw in hits)

    return scores, matched


def ranked_scores(scores: Dict[str, int]) -> List[Tuple[str, int]]:
    return sorted(scores.items(), key=lambda item: (item[1], item[0]), reverse=True)


def pick_agents(scores: Dict[str, int]) -> Tuple[str, str, str]:
    ranked = ranked_scores(scores)
    top_agent, top_score = ranked[0]
    primary = top_agent if top_score > 0 else "Analyst"

    secondary = None
    for agent, score in ranked:
        if agent != primary and score > 0:
            secondary = agent
            break

    if secondary is None:
        secondary = DEFAULT_SUPPORTING.get(primary, "Scrum Master (SM)")

    if top_score >= 4:
        confidence = "vysoka"
    elif top_score >= 2:
        confidence = "stredna"
    else:
        confidence = "nizka"

    return primary, secondary, confidence


def build_result(text: str) -> Dict[str, object]:
    normalized = normalize(text)
    scores, matched = score_request(normalized)
    primary, supporting, confidence = pick_agents(scores)
    sorted_scores = ranked_scores(scores)

    return {
        "primary_agent": primary,
        "primary_agent_alias_sk": AGENT_ALIASES_SK.get(primary, primary),
        "supporting_agent": supporting,
        "supporting_agent_alias_sk": AGENT_ALIASES_SK.get(supporting, supporting),
        "confidence": confidence,
        "matched_keywords": matched.get(primary, []),
        "rationale": (
            f"Poziadavka najviac zodpoveda agentovi {primary} podla klucovych signalov."
            if matched.get(primary)
            else "Nenasiel sa silny signal; predvolene routovane na Analyst pre upresnenie."
        ),
        "top_scores": [
            {
                "agent": agent,
                "agent_alias_sk": AGENT_ALIASES_SK.get(agent, agent),
                "score": score,
            }
            for agent, score in sorted_scores[:5]
        ],
        "handoff_template": {
            "goal": "",
            "inputs": [],
            "constraints": [],
            "done_criteria": [],
            "first_step": "",
        },
    }


def read_request(arg_text: str | None) -> str:
    if arg_text:
        return arg_text.strip()
    piped = sys.stdin.read().strip()
    return piped


def main() -> int:
    parser = argparse.ArgumentParser(description="Nasmeruj poziadavku na BMAD agenta.")
    parser.add_argument("--request", help="Text poziadavky na klasifikaciu.")
    args = parser.parse_args()

    request = read_request(args.request)
    if not request:
        print("Chyba: zadaj --request alebo posli text cez stdin.", file=sys.stderr)
        return 2

    result = build_result(request)
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
