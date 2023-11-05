// Project Details
let name = document.getElementById("name");
let desc = document.getElementById("desc");
let productName = document.getElementById("productName");
let productDesc = document.getElementById("productDesc");
let userIdeas = document.getElementById("userIdeas");
let trafficDesc = document.getElementById("trafficDesc");

// Landing Page Details
let pageName = null;
let conversionRate = document.getElementById("conversionRate");
let pageHtml = document.getElementById("pageHtml");

document.getElementById("create").addEventListener("click", () => {
    let data = {
        name: name.value,
        desc: desc.value,
        productName: productName.value,
        productDesc: productDesc.value,
        userIdeas: userIdeas.value,
        trafficDesc: trafficDesc.value,
        conversionRate: conversionRate.value,
        pageHtml: pageHtml.value,
        pageName: `Html for ${name.value}`,
    };
    console.log(data);
    fetch("create", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": token,
        },
        body: JSON.stringify(data),
    }).then((e) => {
        //? To be redirect to dashboard
        console.log(e, "redirect");
        window.location = "http://localhost:8000/dashboard";
    });
});
