// <!-- トースト用クリックで表示 -->
function showToast(toastId) {
  const toastElement = document.getElementById(toastId);

  if (toastElement) {
    const toastBootstrap = new bootstrap.Toast(toastElement, {
      autohide: true, // 自動非表示
      delay: 5000, // 5秒後非表示
    });
    toastBootstrap.show();
  }
}
// ボタンをクリックしたときにトーストを表示
document.getElementById("sampleToast").addEventListener("click", function () {
  showToast("showToast");
});

// ページ読み込んだ時にトーストを表示（消えない）
document.addEventListener("DOMContentLoaded", function () {
  const alwaysToastEl = document.getElementById("alwaysShowToast");
  const alwaysToast = new bootstrap.Toast(alwaysToastEl, {
    autohide: false, // 常に表示する設定
  });
  alwaysToast.show(); // ページが読み込まれたら表示
});

//  指定のファイルを読み込んで表示
// ファイルを読み込む関数
function loadFile(fileName, targetElementId) {
  fetch(fileName)
    .then((response) => {
      if (!response.ok) {
        throw new Error("ファイルが読み込めませんでした。");
      }
      return response.text();
    })
    .then((data) => {
      // 読み込んだ内容を指定した要素に表示
      document.getElementById(targetElementId).textContent = data;

      // Prism.jsでハイライトを適用
      Prism.highlightElement(document.getElementById(targetElementId));
    })
    .catch((error) => {
      console.error("エラー:", error);
      document.getElementById(targetElementId).textContent =
        "ファイルの読み込み中にエラーが発生しました。";
    });
}

// HTMLがロードされたときに複数のファイルを読み込む
window.addEventListener("load", function () {
  loadFile("../../Sample/src/001cdn.txt", "sourceCode001"); // ファイルを読込
  loadFile("../../Sample/src/011grid.txt", "sourceCode011"); // ファイルを読込
  loadFile("../../Sample/src/021icon.txt", "sourceCode021"); // ファイルを読込
  loadFile("../../Sample/src/031font.txt", "sourceCode031"); // ファイルを読込
  loadFile("../../Sample/src/032font.txt", "sourceCode032"); // ファイルを読込
  loadFile("../../Sample/src/033font.txt", "sourceCode033"); // ファイルを読込
  loadFile("../../Sample/src/041border.txt", "sourceCode041"); // ファイルを読込
  loadFile("../../Sample/src/042border.txt", "sourceCode042"); // ファイルを読込
  loadFile("../../Sample/src/043border.txt", "sourceCode043"); // ファイルを読込
  loadFile("../../Sample/src/044border.txt", "sourceCode044"); // ファイルを読込
  loadFile("../../Sample/src/051hr.txt", "sourceCode051"); // ファイルを読込
  loadFile("../../Sample/src/061table.txt", "sourceCode061"); // ファイルを読込
  loadFile("../../Sample/src/062table.txt", "sourceCode062"); // ファイルを読込
  loadFile("../../Sample/src/071button.txt", "sourceCode071"); // ファイルを読込
  loadFile("../../Sample/src/072button.txt", "sourceCode072"); // ファイルを読込
  loadFile("../../Sample/src/073button.txt", "sourceCode073"); // ファイルを読込
  loadFile("../../Sample/src/081textbox.txt", "sourceCode081"); // ファイルを読込
  loadFile("../../Sample/src/091list.txt", "sourceCode091"); // ファイルを読込
  loadFile("../../Sample/src/092list.txt", "sourceCode092"); // ファイルを読込
  loadFile("../../Sample/src/093list.txt", "sourceCode093"); // ファイルを読込
  loadFile("../../Sample/src/094list.txt", "sourceCode094"); // ファイルを読込
  loadFile("../../Sample/src/101floating.txt", "sourceCode101"); // ファイルを読込
  loadFile("../../Sample/src/111radio.txt", "sourceCode111"); // ファイルを読込
  loadFile("../../Sample/src/121check.txt", "sourceCode121"); // ファイルを読込
  loadFile("../../Sample/src/131file.txt", "sourceCode131"); // ファイルを読込
  loadFile("../../Sample/src/141color.txt", "sourceCode141"); // ファイルを読込
  loadFile("../../Sample/src/151slider.txt", "sourceCode151"); // ファイルを読込
  loadFile("../../Sample/src/161date.txt", "sourceCode161"); // ファイルを読込
  loadFile("../../Sample/src/171page.txt", "sourceCode171"); // ファイルを読込
  loadFile("../../Sample/src/181budge.txt", "sourceCode181"); // ファイルを読込
  loadFile("../../Sample/src/182budge.txt", "sourceCode182"); // ファイルを読込
  loadFile("../../Sample/src/183budge.txt", "sourceCode183"); // ファイルを読込
  loadFile("../../Sample/src/184budge.txt", "sourceCode184"); // ファイルを読込
  loadFile("../../Sample/src/191progress.txt", "sourceCode191"); // ファイルを読込
  loadFile("../../Sample/src/201spinner.txt", "sourceCode201"); // ファイルを読込
  loadFile("../../Sample/src/202spinner.txt", "sourceCode202"); // ファイルを読込
  loadFile("../../Sample/src/211image.txt", "sourceCode211"); // ファイルを読込
  loadFile("../../Sample/src/221popover.txt", "sourceCode221"); // ファイルを読込
  loadFile("../../Sample/src/231toasts.txt", "sourceCode231"); // ファイルを読込
  loadFile("../../Sample/src/241tooltips.txt", "sourceCode241"); // ファイルを読込
  loadFile("../../Sample/src/251Alert.txt", "sourceCode251"); // ファイルを読込
});

// ツールチップの初期化
const tooltipTriggerList = document.querySelectorAll(
  '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);

// ボタンで表示/非表示を切り替える処理
document.querySelectorAll(".toggleTextButton").forEach((button) => {
  button.addEventListener("click", function () {
    const targetId = button.getAttribute("data-target");
    const textArea = document.getElementById(targetId);
    // document.getElementById(".toggleTextButton").addEventListener("click", function () {
    // const textArea = document.getElementById("readonlyText");
    // const button = document.getElementById("toggleTextButton");
    // テキストエリアの表示/非表示を切り替え
    if (textArea.style.display === "none" || textArea.style.display === "") {
      textArea.style.display = "block"; // 表示
      button.innerHTML =
        '<i id="foldericon" class="bi bi-folder2-open"></i> HTMLを非表示';
    } else {
      textArea.style.display = "none"; // 非表示
      button.innerHTML =
        '<i id="foldericon" class="bi bi-folder"></i> HTMLを表示';
    }
  });
});

//  <!-- クリップボード用関数 -->
function copyToClipboard(id) {
  // 選択範囲を取得
  const selection = window.getSelection();
  const selectedText = selection.toString();
  // 特定の要素を取得
  const pre = document.getElementById(id);

  try {
    // 選択範囲が空でない場合にコピー
    if (selectedText) {
      const range = selection.getRangeAt(0);
    } else {
      // 選択範囲がなかったら
      const range = document.createRange();
      range.selectNode(pre);
      window.getSelection().removeAllRanges(); // 現在の選択をクリア
      window.getSelection().addRange(range); // 新しい範囲を選択
    }
    // クリップボードにコピー
    document.execCommand("copy");
    const threeDigitId = ("0" + id.slice(id.length - 3)).slice(-3); // 3桁の数字を取り出してゼロパディング
    const icon = document.getElementById("clipicon" + threeDigitId);
    // 現在のアイコンのクラスをチェック
    if (icon.classList.contains("bi-clipboard2-fill")) {
      icon.classList.remove("bi-clipboard2-fill");
      icon.classList.add("bi-clipboard2-check"); // 変更するアイコンのクラス
    } else {
      icon.classList.remove("bi-clipboard2-check");
      icon.classList.add("bi-clipboard2-fill"); // 元のアイコンに戻す
    }

    // window.getSelection().removeAllRanges(); // 現在の選択をクリア

    // コピー成功時のフィードバック
    document.getElementById("feedback").innerHTML =
      '<div class="alert alert-success">コピーしました！</div>';
  } catch (err) {
    // コピー失敗時のフィードバック
    document.getElementById("feedback").innerHTML =
      '<div class="alert alert-danger">コピーに失敗しました。</div>';
  }

  // 選択をクリア
  window.getSelection().removeAllRanges();
}
