# Document-Driven Development

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | **Français**

Une compétence utilisable par n'importe quel agent de code pour transformer une idée en logiciel qui fonctionne : s'accorder d'abord sur le cœur métier, vérifier ce qui existe déjà, écrire des documents courts, puis prouver le résultat avec des vérifications exécutables.

> Les 15 minutes gagnées en sautant la spécification se paient en 3 heures de débogage. Lent au départ, rapide sur la durée.

## Pour qui

Toute personne qui construit avec un agent IA, technique ou non. L'agent adapte ses questions à son interlocuteur :

- **Développeurs** : pas de questions de base, mais il insiste sur les utilisateurs et les règles métier avant le choix de la stack.
- **Designers, commerciaux, finance, opérations, fondateurs** : aucune question technique. L'agent demande des situations réelles (« racontez-moi votre dernière vente, étape par étape »), propose des brouillons à corriger et prend lui-même les décisions techniques.

## Fonctionnement

```
comprendre la personne → s'accorder sur le cœur métier → vérifier l'existant → intent / spec / plan → construire par tranches → vérifications au vert → jalon
```

1. **Le cœur métier d'abord.** Qui l'utilise, le vrai déroulé, les règles, les exceptions et ce que « ça marche » veut dire, en mots simples.
2. **Ne pas construire en vase clos.** Chercher les produits existants, les pratiques du secteur, l'open source et les bibliothèques. Pour chaque partie : utiliser tel quel, adapter ou construire.
3. **Des documents courts.** `intent.md` (pourquoi, pour qui, ce qu'on ne fait pas), `spec.md` (déroulé, règles, critères vérifiables), `plan.md` (décisions et options écartées), `roadmap.md` (versions et jalons, facultatif). Seulement ce que le code ne montre pas.
4. **Le prouver.** Chaque critère d'acceptation devient une vérification qui passe ou échoue, une seule commande les lance toutes, les règles impératives sont imposées par l'outillage, les revues se font par rapport à la spec, et chaque bug devient une nouvelle vérification.
5. **Un processus à la mesure de l'enjeu.** Un petit changement tient en deux phrases et une exécution des vérifications ; un nouveau produit suit le processus complet.

## Installation

La compétence est du Markdown simple au format ouvert Agent Skills ; elle fonctionne avec n'importe quel modèle.

**Une commande, n'importe quel agent** (Claude Code, Cursor, Codex, etc. ; nécessite Node.js) :

```bash
npx skills add s87343472/document-driven-development
```

**Plugin Claude Code** (peut se mettre à jour automatiquement à chaque nouvelle version) :

```text
/plugin install document-driven-development --marketplace s87343472/document-driven-development
```

Les options ci-dessous installent à la main.

**Claude Code, à la main**

```bash
# ce projet seulement
mkdir -p .claude/skills && cp -r skills/document-driven-development .claude/skills/
# tous les projets
cp -r skills/document-driven-development ~/.claude/skills/
```

Pour empêcher le déclenchement automatique, ajoutez `disable-model-invocation: true` dans le frontmatter de votre copie locale et appelez-la avec `/document-driven-development`.

**Claude.ai ou l'API Claude** : compressez le dossier `skills/document-driven-development` en zip et importez-le comme compétence.

**Autres agents** (Codex, Cursor, Gemini CLI, etc.) : copiez le dossier dans le répertoire de compétences de l'outil s'il prend en charge Agent Skills. Sinon, ajoutez une ligne à votre `AGENTS.md` ou fichier de règles :

```
For new products, new features or changes to business behaviour, follow skills/document-driven-development/SKILL.md.
```

**Chat simple** : collez `SKILL.md` dans la conversation et ajoutez les fichiers de `references/` en arrivant à l'étape concernée.

## Contenu

```
skills/document-driven-development/
├── SKILL.md                 comportement principal, toujours chargé
└── references/              chargés seulement si nécessaire
    ├── discovery.md         questions selon le profil, canevas du cœur métier
    ├── prior-art.md         recherche de l'existant, utiliser / adapter / construire
    ├── templates.md         modèles intent, roadmap, spec, plan, avec un exemple
    ├── verification.md      vérifications, application des règles, revue, régression
    └── principles.md        raisonnement et anti-patterns
scripts/check.py             auto-vérification du dépôt, aussi lancée en CI
.claude-plugin/               entrée de la marketplace de plugins Claude Code
```

## Historique

- **3.0 (2026-10)**
  - Ajouts : questions adaptées au profil (développeur, designer, commercial, finance, opérations, fondateur) ; recherche commune du cœur métier ; étude de l'existant avec décision utiliser / adapter / construire ; couche de vérification (vérifications exécutables, une commande, règles imposées, revue selon la spec, bugs transformés en vérifications) ; profondeur du processus selon l'enjeu.
  - Retraits, car les modèles actuels s'en chargent seuls : décrire la stack et l'arborescence dans `plan.md`, documenter un code existant avant de le modifier, les longs modèles, et la règle « jamais de code sans documents » pour les petits changements.
  - Dépôt : uniquement des champs de frontmatter portables (l'ancien `disable-auto-invoke` n'était pas un champ valide et était ignoré), références dans leur propre dossier, fichiers obsolètes supprimés, auto-vérification et CI ajoutées ; installation en une commande via `npx skills` et la marketplace de plugins Claude Code.
- **2026-06** : roadmap.md, colonne vertébrale d'architecture, jalons de validation, documents comme runtime.
- **2026-03** : découpage en cœur, modèles et principes pour économiser le contexte.
- **2026-01** : première version.

## Série d'articles

La méthode vient de la série en neuf parties « Le nouveau paradigme du code à l'ère de l'IA » (en chinois) sur [sagasu.art](https://www.sagasu.art/).

## Licence et auteur

MIT. Créé par SagaSu : [sagasu.art](https://www.sagasu.art/) · [@sujingshen](https://x.com/sujingshen)
