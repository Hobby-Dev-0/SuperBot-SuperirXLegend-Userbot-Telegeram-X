name: LEGENDX

on: push

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v2

      - name: Find and Replace

        uses: jacobtomlinson/gha-find-replace@master

        with:

          find: "from_id"

          replace: "sender_id"

      - name: Create Pull Request

        uses: stefanzweifel/git-auto-commit-action@v4

        with:

          commit_message: 'Replaced New Username'

          commit_options: '--no-verify'

          repository: .

          commit_user_name: LEGENDXOP

          commit_user_email: legendxx0837@gmail.com