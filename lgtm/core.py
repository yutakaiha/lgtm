import click


@click.command()
def cli():
    # LGTM画像作成ツール
    lgtm()
    click.echo("lgtm")  # 動作確認用


def lgtm():
    pass
