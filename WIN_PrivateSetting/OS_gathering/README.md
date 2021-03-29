Ansible Role: OS-Windows2019/WIN_PrivateSetting/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2019に関するプライバシー設定についての情報の取得を行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL7）
  * Ansible バージョン 2.7 以上 (動作確認バージョン 2.7, 2.9)
  * Python バージョン 3.x  (動作確認バージョン 3.6)
- 管理対象マシン
  * Windows Server 2019

# Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへPowershell接続できる必要があります。
- 管理対象マシン
  * Windows Server 2019
  * Powershell3.0+

# Dependencies

本ロールでは、以下のロール、共通部品を利用しています。

- gathering ロール
- パラメータ生成共通部品(parameter_generate)

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス | 
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス | 
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド | 

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_PrivateSetting/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── パラメータ生成対象/  # 収集データ
                        └── command/
                               ・・・
~~~

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_PrivateSetting.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_PrivateSetting.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_PrivateSetting` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`location` | 「設定」「プライバシー」「アプリのアクセス許可」「位置情報」の「デバイスの位置情報 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`webcam` | 「設定」「プライバシー」「アプリのアクセス許可」「カメラ」の「デバイスのカメラ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`microphone` | 「設定」「プライバシー」「アプリのアクセス許可」「マイク」の「デバイスのマイク アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userNotificationListener` | 「設定」「プライバシー」「アプリのアクセス許可」「通知」の「デバイスの通知 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userAccountInformation` | 「設定」「プライバシー」「アプリのアクセス許可」「アカウント情報」の「デバイスのアカウント情報 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`contacts` | 「設定」「プライバシー」「アプリのアクセス許可」「連絡先」の「デバイスの連絡先 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`appointments` | 「設定」「プライバシー」「アプリのアクセス許可」「カレンダー」の「デバイスのカレンダー アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`phoneCallHistory` | 「設定」「プライバシー」「アプリのアクセス許可」「通話履歴」の「デバイスの通話履歴 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`email` | 「設定」「プライバシー」「アプリのアクセス許可」「メール」の「デバイスのメール アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userDataTasks` | 「設定」「プライバシー」「アプリのアクセス許可」「タスク」の「デバイスのタスク アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`chat` | 「設定」「プライバシー」「アプリのアクセス許可」「メッセージング」の「デバイスのメッセージング アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`radios` | 「設定」「プライバシー」「アプリのアクセス許可」「無線」の「デバイスの無線 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`bluetoothSync` | 「設定」「プライバシー」「アプリのアクセス許可」「他のデバイス」の「ペアリングされていないデバイスとの通信許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`appDiagnostics` | 「設定」「プライバシー」「アプリのアクセス許可」「アプリの診断」の「デバイスのアプリの診断 アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`documentsLibrary` | 「設定」「プライバシー」「アプリのアクセス許可」「ドキュメント」の「デバイスのドキュメントライブラリ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`picturesLibrary` | 「設定」「プライバシー」「アプリのアクセス許可」「ピクチャ」の「デバイスのピクチャライブラリ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`videosLibrary` | 「設定」「プライバシー」「アプリのアクセス許可」「ビデオ」の「デバイスのビデオライブラリ アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`broadFileSystemAccess` | 「設定」「プライバシー」「アプリのアクセス許可」「ファイルシステム」の「デバイスのファイルシステム アクセス許可」に該当<br>Allow ： オン<br>Deny ： オフ | 

### Example
~~~
VAR_WIN_PrivateSetting:
  appDiagnostics: Allow
  appointments: Allow
  bluetoothSync: Allow
  broadFileSystemAccess: Allow
  chat: Allow
  contacts: Allow
  documentsLibrary: Allow
  email: Allow
  location: Allow
  microphone: Allow
  phoneCallHistory: Allow
  picturesLibrary: Allow
  radios: Allow
  userAccountInformation: Allow
  userDataTasks: Allow
  userNotificationListener: Allow
  videosLibrary: Allow
  webcam: Allow
~~~

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2019
    │         └── WIN_PrivateSetting/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── tasks/
    │                   │      check.yml
    │                   │      gathering.yml
    │                   │      generate.yml
    │                   │      main.yml
    │                   │── vars/
    │                   │      gathering_definition.yml
    │                   └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2019/WIN_PrivateSetting/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_PrivateSetting/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_PrivateSetting.yml  # パラメータ
~~~

## パラメータ再利用

以下の例では、生成したパラメータを使用してOSの設定を変更します。

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2019/WIN_PrivateSetting/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_PrivateSetting.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
~~~

# Remarks
-------

# License
-------

# Copyright
---------
Copyright (c) 2021 NEC Corporation

# Author Information
------------------
NEC Corporation
