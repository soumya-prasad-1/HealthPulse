/* =========================================================
   HEALTHPULSE
   COMMON JAVASCRIPT
   ========================================================= */


/* =========================================================
   MOBILE MENU
   ========================================================= */

function toggleMobileMenu() {

    const mobileMenu =
        document.getElementById("mobileMenu");

    if (!mobileMenu) {
        return;
    }

    mobileMenu.classList.toggle("open");

}


/* =========================================================
   DOM CONTENT LOADED
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {


    /* =====================================================
       MOBILE MENU
       ===================================================== */

    const mobileMenu =
        document.getElementById("mobileMenu");


    const mobileMenuButton =
        document.querySelector(".mobile-menu-btn");


    /* -----------------------------------------------------
       CLOSE MOBILE MENU AFTER CLICKING A LINK
       ----------------------------------------------------- */

    const mobileLinks =
        document.querySelectorAll(".mobile-menu a");


    mobileLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            if (mobileMenu) {

                mobileMenu.classList.remove("open");

            }

        });

    });


    /* =====================================================
       NAVBAR SCROLL EFFECT
       ===================================================== */

    const navbar =
        document.querySelector(".navbar");


    function updateNavbar() {

        if (!navbar) {
            return;
        }


        if (window.scrollY > 30) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    }


    window.addEventListener(
        "scroll",
        updateNavbar
    );


    updateNavbar();


    /* =====================================================
       SCROLL REVEAL
       ===================================================== */

    const revealElements =
        document.querySelectorAll(".reveal");


    if ("IntersectionObserver" in window) {

        const revealObserver =
            new IntersectionObserver(

                function (entries) {

                    entries.forEach(function (entry) {

                        if (entry.isIntersecting) {

                            entry.target.classList.add("show");

                            revealObserver.unobserve(
                                entry.target
                            );

                        }

                    });

                },

                {
                    threshold: 0.12
                }

            );


        revealElements.forEach(function (element) {

            revealObserver.observe(element);

        });

    } else {

        /* Fallback for older browsers */

        revealElements.forEach(function (element) {

            element.classList.add("show");

        });

    }


    /* =====================================================
       SMOOTH INTERNAL LINKS
       ===================================================== */

    const internalLinks =
        document.querySelectorAll(
            'a[href^="#"]'
        );


    internalLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const targetId =
                link.getAttribute("href");


            if (
                targetId &&
                targetId !== "#"
            ) {

                const target =
                    document.querySelector(targetId);


                if (target) {

                    event.preventDefault();


                    target.scrollIntoView({

                        behavior: "smooth",

                        block: "start"

                    });

                }

            }

        });

    });


    /* =====================================================
       CLOSE MOBILE MENU WHEN CLICKING OUTSIDE
       ===================================================== */

    document.addEventListener(
        "click",
        function (event) {

            if (!mobileMenu) {
                return;
            }


            if (!mobileMenuButton) {
                return;
            }


            const clickedInsideMenu =
                mobileMenu.contains(event.target);


            const clickedMenuButton =
                mobileMenuButton.contains(event.target);


            if (
                !clickedInsideMenu &&
                !clickedMenuButton
            ) {

                mobileMenu.classList.remove("open");

            }

        }
    );


});