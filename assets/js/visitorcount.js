async function get_visitors() {
  const countEl  = document.getElementById("visitor-count");
  const inlineEl = document.getElementById("visitor-inline");

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 6000);

  try {
    const response = await fetch(
      "https://qfky693v2f.execute-api.eu-west-2.amazonaws.com/default/terraform_lambda_func",
      { method: "GET", signal: controller.signal }
    );
    clearTimeout(timeout);

    if (!response.ok) throw new Error("Failed to fetch visitor count");

    const data  = await response.json();
    const count = data["count"] || data["visitor_count"] || data;

    if (count) {
      const formatted = Number(count).toLocaleString();
      if (countEl)  countEl.textContent  = formatted;
      if (inlineEl) inlineEl.textContent = formatted;
    }
  } catch (err) {
    clearTimeout(timeout);
    if (countEl)  countEl.textContent  = "—";
    if (inlineEl) inlineEl.textContent = "—";
  }
}

get_visitors();
