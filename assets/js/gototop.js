const goTopBtn = document.getElementById("goTopBtn");

if (goTopBtn) {
    window.addEventListener("scroll", function () {
        const scrolled = document.body.scrollTop > 200 || document.documentElement.scrollTop > 200;
        goTopBtn.classList.toggle("visible", scrolled);
    });

    goTopBtn.addEventListener("click", function (e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
}
