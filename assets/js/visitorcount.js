// GET API REQUEST
async function get_visitors() {
  // call post api request function
  //await post_visitor();
  try {
    let response = await fetch(
      "https://qfky693v2f.execute-api.eu-west-2.amazonaws.com/default/terraform_lambda_func", // API Gateway URL
      {
        method: "GET",
      }
    );
    let data = await response.json();
    document.getElementById("visitors").innerHTML = data["count"];
    console.log(data);
    return data;
  } catch (err) {
    console.error(err);
  }
}

get_visitors();
