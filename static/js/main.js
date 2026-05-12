console.log("Surve Prozone Loaded 🚀");

/* NAVBAR EFFECT */

const navbar = document.querySelector("nav");

window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
        navbar.classList.add("bg-black/60", "border-white/10");
    } else {
        navbar.classList.remove("bg-black/60", "border-white/10");
    }
});

/* MOBILE MENU */

const menuBtn = document.getElementById("menu-btn");
const closeMenu = document.getElementById("close-menu");
const mobileMenu = document.getElementById("mobile-menu");
const menuOverlay = document.getElementById("menu-overlay");

const closeMobileMenu = () => {
    if (mobileMenu) mobileMenu.style.right = "-100%";
    if (menuOverlay) menuOverlay.classList.add("hidden");
    document.body.style.overflow = "auto";
};

if (menuBtn && mobileMenu && menuOverlay) {
    menuBtn.addEventListener("click", () => {
        mobileMenu.style.right = "0";
        menuOverlay.classList.remove("hidden");
        document.body.style.overflow = "hidden";
    });
}

if (closeMenu) {
    closeMenu.addEventListener("click", closeMobileMenu);
}

if (menuOverlay) {
    menuOverlay.addEventListener("click", closeMobileMenu);
}

if (mobileMenu) {
    const mobileLinks = mobileMenu.querySelectorAll("a");

    mobileLinks.forEach((link) => {
        link.addEventListener("click", closeMobileMenu);
    });
}

/* COUNTER ANIMATION */

const counters = document.querySelectorAll(".counter");

const startCounter = (counter) => {
    const target = +counter.getAttribute("data-target");
    let count = 0;
    const speed = target / 100;

    const updateCounter = () => {
        count += speed;

        if (count < target) {
            counter.innerText = Math.ceil(count);
            requestAnimationFrame(updateCounter);
        } else {
            counter.innerText = target + "+";
        }
    };

    updateCounter();
};

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            startCounter(entry.target);
            counterObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5
});

counters.forEach((counter) => {
    counterObserver.observe(counter);
});

/* ACTIVE NAVBAR LINKS */

const sections = document.querySelectorAll("section");

const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach((section) => {

        const sectionTop = section.offsetTop - 120;

        const sectionHeight = section.clientHeight;

        if (scrollY >= sectionTop) {

            current = section.getAttribute("id");

        }

    });

    navLinks.forEach((link) => {

        link.classList.remove(
            "text-blue-400"
        );

        if (link.getAttribute("href") === `#${current}`) {

            link.classList.add(
                "text-blue-400"
            );

        }

    });

});


/* ENQUIRY FORM LOADING STATE */

const enquiryForm = document.getElementById("enquiry-form");
const submitBtn = document.getElementById("submit-btn");
const submitText = document.getElementById("submit-text");
const submitLoader = document.getElementById("submit-loader");

if (enquiryForm && submitBtn && submitText && submitLoader) {
    enquiryForm.addEventListener("submit", () => {
        submitBtn.disabled = true;
        submitBtn.classList.add("opacity-70", "cursor-not-allowed");
        submitText.innerText = "Submitting...";
        submitLoader.classList.remove("hidden");
    });
}

/* GALLERY FILTER */

const filterButtons = document.querySelectorAll(".gallery-filter");
const galleryItems = document.querySelectorAll(".gallery-item");

if (filterButtons.length && galleryItems.length) {
    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const filter = button.getAttribute("data-filter");

            filterButtons.forEach((btn) => {
                btn.classList.remove("active-filter", "border-blue-500", "bg-blue-500/20", "text-blue-300");
                btn.classList.add("border-white/10", "bg-white/5");
            });

            button.classList.add("active-filter", "border-blue-500", "bg-blue-500/20", "text-blue-300");
            button.classList.remove("border-white/10", "bg-white/5");

            galleryItems.forEach((item) => {
                const category = item.getAttribute("data-category");

                if (filter === "all" || filter === category) {
                    item.classList.remove("hidden");
                } else {
                    item.classList.add("hidden");
                }
            });
        });
    });
}