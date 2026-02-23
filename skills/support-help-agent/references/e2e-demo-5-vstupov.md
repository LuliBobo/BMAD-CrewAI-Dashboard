# E2E Demo (5 vstupov)

Tento demo scenar ukazuje:
1. presnu odpoved `support-help-agent`,
2. nasledny handoff z `orchestrator` routera.

## Scenar 1

**Vstup pouzivatela**
`Neviem, ci mam najprv pisat PRD alebo riesit architekturu.`

**Presna odpoved support-help-agent**
```markdown
Odporucany Agent: Orchestrator
Alternativa: Product Manager (PM)
Preco:
- Poziadavka zasahuje viac roli (PM aj Architect), preto je vhodne najprv spravit routovanie.

Dalsi Krok:
- Spusti routovanie cez Orchestrator pre presny vyber primarneho a podporneho agenta.

Ak Chces, Pokracuj:
- python3 ../orchestrator/scripts/route_orchestrator.py --request "Neviem, ci mam najprv pisat PRD alebo riesit architekturu."
```

**Nasledny handoff na Orchestrator (vystup routera)**
```markdown
Primarny Agent: Product Manager (PM)
Podporny Agent: Architect
Istota: nizka
Preco:
- Poziadavka najviac zodpoveda agentovi Product Manager (PM) podla klucovych signalov.
- Matchnute klucove slova: prd
```

## Scenar 2

**Vstup pouzivatela**
`Potrebujem rychlo nasadit release cez CI/CD a potom doplnit release notes.`

**Presna odpoved support-help-agent**
```markdown
Odporucany Agent: Orchestrator
Alternativa: Release/DevOps Agent
Preco:
- Request kombinuje release aj dokumentaciu, preto je lepsie urobit najprv orchestraciu.

Dalsi Krok:
- Spusti Orchestrator router a nechaj urcit poradie medzi Release/DevOps a Tech Writer.

Ak Chces, Pokracuj:
- python3 ../orchestrator/scripts/route_orchestrator.py --request "Potrebujem rychlo nasadit release cez CI/CD a potom doplnit release notes."
```

**Nasledny handoff na Orchestrator (vystup routera)**
```markdown
Primarny Agent: Tech Writer / Documentarian
Podporny Agent: Release/DevOps Agent
Istota: stredna
Preco:
- Poziadavka najviac zodpoveda agentovi Tech Writer / Documentarian podla klucovych signalov.
- Matchnute klucove slova: release notes
```

## Scenar 3

**Vstup pouzivatela**
`Mam bug v produkte, chcem opravu, testy a code review.`

**Presna odpoved support-help-agent**
```markdown
Odporucany Agent: Orchestrator
Alternativa: Developer (Dev)
Preco:
- Ide o build + QA + review fazu, preto treba najprv urcit primarneho vlastnika cez orchestraciu.

Dalsi Krok:
- Spusti routovanie a pouzi vysledok ako handoff pre implementacny tok.

Ak Chces, Pokracuj:
- python3 ../orchestrator/scripts/route_orchestrator.py --request "Mam bug v produkte, chcem opravu, testy a code review."
```

**Nasledny handoff na Orchestrator (vystup routera)**
```markdown
Primarny Agent: Code Reviewer
Podporny Agent: Developer (Dev)
Istota: stredna
Preco:
- Poziadavka najviac zodpoveda agentovi Code Reviewer podla klucovych signalov.
- Matchnute klucove slova: code review
```

## Scenar 4

**Vstup pouzivatela**
`Sme v polovici sprintu a klient mení prioritu, čo teraz?`

**Presna odpoved support-help-agent**
```markdown
Odporucany Agent: Orchestrator
Alternativa: Correct-Course Agent
Preco:
- Je to mid-sprint zmena smeru, kde je dobre spravit najprv routovanie a potom replanning.

Dalsi Krok:
- Spusti Orchestrator router a nasledne odovzdaj task na Correct-Course/SM podla vysledku.

Ak Chces, Pokracuj:
- python3 ../orchestrator/scripts/route_orchestrator.py --request "Sme v polovici sprintu a klient meni prioritu, co teraz?"
```

**Nasledny handoff na Orchestrator (vystup routera)**
```markdown
Primarny Agent: Scrum Master (SM)
Podporny Agent: Developer (Dev)
Istota: nizka
Preco:
- Poziadavka najviac zodpoveda agentovi Scrum Master (SM) podla klucovych signalov.
- Matchnute klucove slova: sprint
```

## Scenar 5

**Vstup pouzivatela**
`Chcem spustit brainstorming novych funkcionalit a potom to zladit s biznis cielmi.`

**Presna odpoved support-help-agent**
```markdown
Odporucany Agent: Orchestrator
Alternativa: Idea Coach / Brainstorming Coach
Preco:
- Request pokryva ideaciu aj strategiu, preto je vhodne najprv orchestracne routovanie.

Dalsi Krok:
- Spusti Orchestrator router a pouzi vystupne poradie agentov pre navazny workflow.

Ak Chces, Pokracuj:
- python3 ../orchestrator/scripts/route_orchestrator.py --request "Chcem spustit brainstorming novych funkcionalit a potom to zladit s biznis cielmi."
```

**Nasledny handoff na Orchestrator (vystup routera)**
```markdown
Primarny Agent: Idea Coach / Brainstorming Coach
Podporny Agent: Business Strategist
Istota: stredna
Preco:
- Poziadavka najviac zodpoveda agentovi Idea Coach / Brainstorming Coach podla klucovych signalov.
- Matchnute klucove slova: brainstorm, brainstorming
```
