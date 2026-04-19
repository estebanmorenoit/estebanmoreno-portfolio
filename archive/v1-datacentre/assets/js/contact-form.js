document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");

    if (!form) return;

    // Create a status message element below the form actions
    const statusMsg = document.createElement("p");
    statusMsg.id = "form-status";
    statusMsg.setAttribute("role", "status");
    statusMsg.setAttribute("aria-live", "polite");
    statusMsg.style.marginTop = "1em";
    form.appendChild(statusMsg);

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const submitBtn = form.querySelector('input[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.value = "Sending…";
        statusMsg.textContent = "";
        statusMsg.className = "";

        try {
            const response = await fetch(form.action, {
                method: "POST",
                body: new FormData(form),
                headers: { Accept: "application/json" },
            });

            if (response.ok) {
                statusMsg.textContent = "Thank you! Your message has been sent.";
                statusMsg.className = "form-status-success";
                form.reset();
                window.location.hash = "";
            } else {
                statusMsg.textContent = "Oops! Something went wrong. Please try again.";
                statusMsg.className = "form-status-error";
            }
        } catch (err) {
            statusMsg.textContent = "Could not send message. Please check your connection and try again.";
            statusMsg.className = "form-status-error";
        } finally {
            submitBtn.disabled = false;
            submitBtn.value = "Send Message";
        }
    });
});
