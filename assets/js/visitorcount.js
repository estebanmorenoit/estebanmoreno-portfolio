async function get_visitors() {
  const visitorElement = document.getElementById("visitors");
  try {
    const response = await fetch("https://qfky693v2f.execute-api.eu-west-2.amazonaws.com/default/terraform_lambda_func", {
      method: "GET",
    });

    if (!response.ok) throw new Error("Failed to fetch visitor count");

    const data = await response.json();

    // Update visitor count and add animation class
    visitorElement.textContent = data["count"];
    visitorElement.classList.add("loaded");

    console.log("Visitor count:", data);
    return data;
  } catch (err) {
    console.error("Visitor count fetch failed:", err);
    visitorElement.textContent = "N/A";
    visitorElement.classList.add("loaded");
  }
}

get_visitors();
