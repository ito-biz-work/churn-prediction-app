import subprocess

from config.settings import BACKEND_DIR

SCRIPT_PATH = BACKEND_DIR / "scripts" / "run_bulk_prediction.sh"


def test_run_bulk_prediction_sh_success():
    """シェルスクリプトが正常に実行され、終了コード0で終わるか"""

    # シェルスクリプトを裏側で実行する
    result = subprocess.run(
        ["bash", str(SCRIPT_PATH)],
        capture_output=True,  # 出力の録画機能をON（保存）
        text=True,  # 出力を文字列として扱う
        check=False,  # エラー時に例外を発生させない
    )

    # 検証
    assert result.returncode == 0
    assert "バッチ処理が完了しました" in result.stdout
