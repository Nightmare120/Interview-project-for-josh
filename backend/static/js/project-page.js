console.log("hi from project!");

let edited = false;
let changeable = document.querySelectorAll(".changeable");
let saveBtn = document.getElementById("save_changes");

let productName = document.getElementById("productName");
let productDesc = document.getElementById("productDesc");
let userIdeas = document.getElementById("userIdeas");
let trafficDesc = document.getElementById("trafficDesc");

// Landing Page Details
let conversionRate = document.getElementById("conversionRate");
let pageHtml = document.getElementById("pageHtml");

// AB testing
let isAB_Active = 0;
let pageHtml2 = document.getElementById("pageHtml2");

changeable.forEach((e) => {
    e.addEventListener("change", () => {
        console.log("changed");
        edited = true;
        showSaveChangeBtn();
    });
});

saveBtn.addEventListener("click", () => {
    if (edited) {
        saveNewChanges();
    }
});

function showSaveChangeBtn() {
    saveBtn.style.display = "block";
}

function saveNewChanges() {
    console.log("new changes saved!");

    let data = {
        productName: productName.value,
        productDesc: productDesc.value,
        userIdeas: userIdeas.value,
        trafficDesc: trafficDesc.value,
        conversionRate: conversionRate.value,
        pageHtml: pageHtml.value,
        isAB_Active: isAB_Active,
        pageHtml2: pageHtml2.value,
        id: Number(getID()),
    };
    console.log(data);

    fetch("save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": token,
        },
        body: JSON.stringify(data),
    }).then((e) => {
        //? To be redirect to dashboard
        console.log(e, "redirect");
        location.reload();
    });
}

function getID() {
    let url_string = window.location.href;
    let url = new URL(url_string);
    let c = url.searchParams.get("id");
    return c;
}

let ABswitch = document.getElementById("ABswitch");

ABswitch.addEventListener("change", (e) => {
    if (ABswitch.checked) {
        showSecondHtmlBox();
    } else {
        unshowSecondHtmlBox();
    }
});

function showSecondHtmlBox() {
    pageHtml2.parentElement.style.display = "block";
    pageHtml2.parentElement.style.width = "47%";
    pageHtml.parentElement.style.width = "47%";
    pageHtml.nextElementSibling.style.display = "flex";
    isAB_Active = 1;
}

function unshowSecondHtmlBox() {
    pageHtml2.parentElement.style.display = "none";
    pageHtml.parentElement.style.width = "100%";
    pageHtml.nextElementSibling.style.display = "none";
    isAB_Active = 0;
}
