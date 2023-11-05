console.log("Hi from dashboard!");

let delBtn = document.querySelectorAll(".del");

delBtn.forEach((e) => {
    e.addEventListener("click", () => {
        let projectId = e.getAttribute("projectId");
        e.parentElement.parentElement.style.display = "none";
        deleteProject(projectId);
    });
});

function deleteProject(id) {
    fetch("delete", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": token,
        },
        body: JSON.stringify({ id }),
    }).then((e) => {
        console.log(e, "deleted id", id);
    });
}
