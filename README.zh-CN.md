# 文档驱动开发（Document-Driven Development）

[English](README.md) | **简体中文** | [日本語](README.ja.md) | [Français](README.fr.md)

一个能交给任何编程 Agent 使用的技能：先和人一起把业务核心讲清楚，再看看业界有没有现成方案，然后写几份简短文档，最后用能跑的检查证明做对了。

> 你在 prompt 里省下的十五分钟需求描述，会变成三小时的 debug 账单。慢在开头，快在全程。

## 适合谁

所有用 AI Agent 做东西的人，懂不懂技术都行。Agent 会根据对面是谁调整提问方式：

- **工程师**：跳过基础问题，但在选技术栈之前，会一直追问用户是谁、业务规则是什么。
- **设计师、销售、财务、运营、创业者**：不问任何技术问题。Agent 会问真实发生过的事（比如“带我走一遍上一单是怎么成交的”），先给草稿让你改，技术上的决定它自己做。

## 怎么运作

```
看清对面是谁 → 共同确认业务核心 → 查现成方案 → intent / spec / plan → 小步构建 → 检查通过 → 版本关卡
```

1. **业务核心优先。** 谁在用、真实流程怎么走、有哪些规则和例外、怎样算“能用”，用大白话达成一致。
2. **不闭门造车。** 先找现成产品、行业通行做法、开源项目和现成库，每一块都决定是直接用、改一改还是自己做。
3. **文档要短。** `intent.md`（为什么做、给谁用、不做什么），`spec.md`（流程、规则、验收检查），`plan.md`（决策和被否掉的方案），`roadmap.md`（版本和关卡，可选）。只写代码里看不出来的东西。
4. **用检查证明。** 每条验收标准都变成能跑出通过或失败的检查，一条命令跑全部；必须遵守的规则放进工具里强制；审查对照 spec 做；每个 bug 都变成一条新检查。
5. **流程轻重看风险。** 小改动说两三句再跑一遍检查就行，新产品才走完整流程。

## 安装

技能是纯 Markdown，遵循开放的 Agent Skills 格式，任何模型都能用。

**Claude Code**

```bash
# 只用于当前项目
mkdir -p .claude/skills && cp -r skills/document-driven-development .claude/skills/
# 所有项目
cp -r skills/document-driven-development ~/.claude/skills/
```

不想让它自动触发，就在你本地副本的 frontmatter 里加一行 `disable-model-invocation: true`，然后用 `/document-driven-development` 手动调用。

**Claude.ai 或 Claude API**：把 `skills/document-driven-development` 文件夹打包成 zip，作为技能上传。

**其他 Agent**（Codex、Cursor、Gemini CLI 等）：如果工具支持 Agent Skills，把文件夹复制到它的技能目录。不支持的话，在 `AGENTS.md` 或规则文件里加一行：

```
For new products, new features or changes to business behaviour, follow skills/document-driven-development/SKILL.md.
```

**普通对话**：把 `SKILL.md` 贴进对话，进行到对应步骤时再补上 `references/` 里的文件。

## 里面有什么

```
skills/document-driven-development/
├── SKILL.md                 核心行为，每次都会加载
└── references/              需要时才加载
    ├── discovery.md         按人群区分的提问方法、业务核心画布
    ├── prior-art.md         怎么找现成方案，直接用 / 改造 / 自建
    ├── templates.md         intent、roadmap、spec、plan 模板和完整示例
    ├── verification.md      检查、强制规则、审查、回归
    └── principles.md        背后的道理和常见反模式
scripts/check.py             仓库自检脚本，CI 里也会跑
```

## 更新日志

- **3.0（2026-10）**
  - 新增：按人群调整提问（工程师、设计师、销售、财务、运营、创业者）；共同找出业务核心；先查现成方案并决定直接用、改造还是自建；验收层（可运行的检查、一条命令、规则强制、对照 spec 审查、bug 变检查）；流程轻重随风险调整。
  - 删除（现在的模型已经能自己做好）：在 `plan.md` 里写技术栈和目录结构、改老项目前先把现状写成文档、冗长模板，以及小改动也必须先写文档的硬规则。
  - 仓库：只用通用 frontmatter 字段（旧的 `disable-auto-invoke` 不是有效字段，一直被忽略）；参考文件单独放进 references 文件夹；删掉过期文件；新增自检脚本和 CI。
- **2026-06**：roadmap.md、架构主干、版本验证关卡、文档即运行时。
- **2026-03**：拆成核心、模板、原则三份文件，节省上下文。
- **2026-01**：首次发布。

## 系列文章

方法来自 [sagasu.art](https://www.sagasu.art/) 上的九篇系列文章《AI 时代的编程新范式》。

## 许可与作者

MIT。作者 SagaSu：[sagasu.art](https://www.sagasu.art/) · [@sujingshen](https://x.com/sujingshen)
