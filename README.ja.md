# ドキュメント駆動開発（Document-Driven Development）

[English](README.md) | [简体中文](README.zh-CN.md) | **日本語** | [Français](README.fr.md)

どのコーディングエージェントでも使えるスキルです。まず相手と一緒にビジネスの核を言葉にし、既存の解決策を調べ、短いドキュメントを書き、実行できるチェックで結果を証明します。

> 仕様を省いて浮いた15分は、3時間のデバッグとして返ってくる。最初はゆっくり、全体では速く。

## 対象

技術者かどうかを問わず、AIエージェントでものを作るすべての人。エージェントは相手に合わせて質問の仕方を変えます。

- **エンジニア**：基本的な質問は省き、技術選定の前にユーザーとビジネスルールを詰めます。
- **デザイナー、営業、経理、オペレーション、創業者**：技術的な質問はしません。実際の出来事（「直近の商談を最初から順に教えてください」）を聞き、たたき台を見せて直してもらい、技術的な判断はエージェントが行います。

## 仕組み

```
相手を知る → ビジネスの核を合意する → 既存の解決策を調べる → intent / spec / plan → 小さく作る → チェック通過 → ゲート
```

1. **ビジネスの核が先。** 誰が使うか、実際の流れ、ルール、例外、「動いた」と言える状態を平易な言葉で合意します。
2. **ゼロから作らない。** 既存の製品、業界の標準的なやり方、オープンソース、ライブラリを探し、部分ごとに「そのまま使う・手を加える・作る」を決めます。
3. **ドキュメントは短く。** `intent.md`（なぜ、誰のため、作らないもの）、`spec.md`（流れ、ルール、受け入れチェック）、`plan.md`（決定事項と却下した案）、`roadmap.md`（バージョンとゲート、任意）。コードから読み取れないことだけを書きます。
4. **チェックで証明する。** 受け入れ基準はすべて合否が出るチェックにし、1つのコマンドで全部実行します。必ず守るルールはツールで強制し、レビューはspecと照らし合わせ、バグはすべて新しいチェックになります。
5. **重さはリスク次第。** 小さな変更は2〜3文の説明とチェック実行だけ、新しいプロダクトはフルの流れで進めます。

## インストール

スキルはプレーンなMarkdownで、オープンなAgent Skills形式に従っているため、どのモデルでも使えます。

**1コマンドで、どのエージェントでも**（Claude Code、Cursor、Codex など。Node.js が必要）：

```bash
npx skills add s87343472/document-driven-development
```

**Claude Code プラグイン**（新しいバージョンを自動で受け取れます）：

```text
/plugin install document-driven-development --marketplace s87343472/document-driven-development
```

以下は手動でのインストール方法です。

**Claude Code（手動）**

```bash
# このプロジェクトのみ
mkdir -p .claude/skills && cp -r skills/document-driven-development .claude/skills/
# すべてのプロジェクト
cp -r skills/document-driven-development ~/.claude/skills/
```

自動で起動させたくない場合は、ローカルのコピーのfrontmatterに `disable-model-invocation: true` を追加し、`/document-driven-development` で呼び出します。

**Claude.ai または Claude API**：`skills/document-driven-development` フォルダをzipにしてスキルとしてアップロードします。

**その他のエージェント**（Codex、Cursor、Gemini CLI など）：Agent Skillsに対応していればフォルダをそのスキルディレクトリにコピーします。対応していなければ `AGENTS.md` やルールファイルに1行追加します。

```
For new products, new features or changes to business behaviour, follow skills/document-driven-development/SKILL.md.
```

**通常のチャット**：`SKILL.md` を会話に貼り付け、該当ステップに来たら `references/` のファイルを追加します。

## 中身

```
skills/document-driven-development/
├── SKILL.md                 コアの振る舞い、毎回読み込まれる
└── references/              必要なときだけ読み込まれる
    ├── discovery.md         相手のタイプ別の質問法、ビジネスの核キャンバス
    ├── prior-art.md         既存の解決策の探し方、使う・手を加える・作る
    ├── templates.md         intent、roadmap、spec、plan のテンプレートと実例
    ├── verification.md      チェック、強制、レビュー、回帰
    └── principles.md        考え方とアンチパターン
scripts/check.py             リポジトリの自己チェック、CIでも実行
.claude-plugin/               Claude Code プラグインマーケットプレイスの設定
```

## 変更履歴

- **3.0（2026-10）**
  - 追加：相手に合わせたヒアリング（エンジニア、デザイナー、営業、経理、オペレーション、創業者）、ビジネスの核を一緒に見つける手順、既存解決策の調査と「使う・手を加える・作る」の判断、検証レイヤー（実行できるチェック、1コマンド、ルールの強制、specに基づくレビュー、バグのチェック化）、リスクに応じたプロセスの重さ。
  - 削除（現在のモデルが自力でできるため）：`plan.md` への技術スタックとディレクトリ構成の記述、既存コードを変更前に文書化する手順、長いテンプレート、小さな変更でも先に文書を書くという規則。
  - リポジトリ：汎用的なfrontmatterフィールドのみ使用（旧 `disable-auto-invoke` は有効なフィールドではなく無視されていた）、参照ファイルを専用フォルダに分離、古いファイルを削除、自己チェックとCIを追加。`npx skills` と Claude Code プラグインマーケットプレイスで1コマンドインストールに対応。
- **2026-06**：roadmap.md、アーキテクチャの背骨、検証ゲート、ランタイムとしてのドキュメント。
- **2026-03**：コンテキスト効率のためコア・テンプレート・原則に分割。
- **2026-01**：初回リリース。

## 連載記事

この方法は [sagasu.art](https://www.sagasu.art/) の全9回の連載「AI時代の新しいコーディングパラダイム」（中国語）がもとになっています。

## ライセンスと作者

MIT。作者 SagaSu：[sagasu.art](https://www.sagasu.art/) · [@sujingshen](https://x.com/sujingshen)
