document.getElementById("recipeForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const ingredients = document.getElementById("ingredients").value;

    fetch('/recipe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients: ingredients })
    })
    .then(response => response.json())
    .then(data => {
        const recipeList = document.getElementById("recipeList");
        recipeList.innerHTML = ""; // Clear previous results

        if (data.success) {
            const li = document.createElement("li");
            li.classList.add("list-group-item");
            li.textContent = data.recipe;
            recipeList.appendChild(li);
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => console.error("Error:", error));
});
