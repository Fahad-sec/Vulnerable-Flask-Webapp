document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("commentForm");
  const textarea = form.querySelector('textarea[name="content"]');

  // Intentional DOM-XSS preview: using innerHTML Is dangerous on purpose.
  const preview = document.createElement("div");
  preview.style.marginTop = "6px";
  preview.style.fontSize = "12px";
  preview.innerHTML = "<i>live preview (intentionally unsafe)</i>";
  textarea.insertAdjacentElement("afterend", preview);

  textarea.addEventListener("input", () => {
    // DANGEROUS preview - will fix this later.
    preview.innerHTML = textarea.value;
  });
});


