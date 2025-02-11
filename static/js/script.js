// Username validation
document.addEventListener("DOMContentLoaded", function () {
    const usernameInput = document.getElementById("id_username");
    const usernameFeedback = document.createElement("small");
    usernameFeedback.style.color = "red";
    usernameInput.parentNode.appendChild(usernameFeedback);

    usernameInput.addEventListener("input", function () {
        const username = usernameInput.value;

        // Check length validation
        if (username.length < 5) {
            usernameFeedback.textContent = "Username must be at least 5 characters long.";
            return;
        }

        // Check if username is already taken
        fetch(`/members/check-username/?username=${username}`)
            .then(response => response.json())
            .then(data => {
                if (data.is_taken) {
                    usernameFeedback.textContent = "This username is already taken. Please choose another.";
                } else {
                    usernameFeedback.textContent = "";
                }
            })
            .catch(error => console.error("Error checking username:", error));
    });
});

// Real-time search filter
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInput");
    const eventCards = document.querySelectorAll(".event-card");

    searchInput.addEventListener("input", function () {
        const searchQuery = searchInput.value.toLowerCase();

        eventCards.forEach(card => {
            const eventName = card.getAttribute("data-name");
            const eventCategory = card.getAttribute("data-category");

            if (eventName.includes(searchQuery) || eventCategory.includes(searchQuery)) {
                card.style.display = "block"; // Show matching events
            } else {
                card.style.display = "none"; // Hide non-matching events
            }
        });
    });
});
