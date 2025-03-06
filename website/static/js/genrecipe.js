document.getElementById("recipeForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const ingredients = document.getElementById("ingredients").value;
    const submitButton = document.getElementById("submitButton");
    const recipeList = document.getElementById("recipeList");

    submitButton.disabled = true; // Disable button while processing
    recipeList.innerHTML = "<li class='list-group-item'>Generating recipes...</li>"; // Show loading text

    fetch('/recipe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients: ingredients })
    })
    .then(response => response.json())
    .then(data => {
        recipeList.innerHTML = ""; // Clear loading text

        if (data.success) {
            const recipes = data.recipe.split("---"); // Split recipes by separator
            recipes.forEach(recipe => {
                if (recipe.trim() !== "") {
                    const recipeItem = document.createElement("li");
                    recipeItem.classList.add("list-group-item");
                    recipeItem.innerHTML = recipe.trim();
                    recipeList.appendChild(recipeItem);
                }
            });
        } else {
            recipeList.innerHTML = "<li class='list-group-item text-danger'>Error: " + data.error + "</li>";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        recipeList.innerHTML = "<li class='list-group-item text-danger'>An error occurred. Please try again.</li>";
    })
    .finally(() => {
        submitButton.disabled = false; // Re-enable button after response
    });
});
