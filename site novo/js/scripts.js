document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");

    menuToggle.addEventListener("click", function () {
        menu.classList.toggle("active");
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const texto = "Marketing Digital de Alto Impacto!";
    let i = 0;
    function digitar() {
        if (i < texto.length) {
            document.getElementById("typing").innerHTML += texto.charAt(i);
            i++;
            setTimeout(digitar, 100);
        }
    }
    digitar();
});


document.addEventListener("DOMContentLoaded", function () {
    const sobreSection = document.querySelector("#sobre");

    function checkScroll() {
        const position = sobreSection.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            sobreSection.classList.add("visible");
        }
    }

    window.addEventListener("scroll", checkScroll);
});


document.addEventListener("DOMContentLoaded", function () {
    const planosSection = document.querySelector("#planos");

    function checkScroll() {
        const position = planosSection.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            planosSection.classList.add("visible");
        }
    }

    window.addEventListener("scroll", checkScroll);
});


document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".carousel");
    const images = document.querySelectorAll(".carousel img");
    const prevBtn = document.querySelector(".prev-btn");
    const nextBtn = document.querySelector(".next-btn");

    let index = 0;

    function showImage(i) {
        if (i < 0) {
            index = images.length - 1;
        } else if (i >= images.length) {
            index = 0;
        } else {
            index = i;
        }

        carousel.style.transform = `translateX(${-index * 100}%)`;
    }

    prevBtn.addEventListener("click", () => {
        showImage(index - 1);
    });

    nextBtn.addEventListener("click", () => {
        showImage(index + 1);
    });

    // Auto-slide a cada 5 segundos
    setInterval(() => {
        showImage(index + 1);
    }, 5000);
});


document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".carousel-depoimentos");
    const depoimentos = document.querySelectorAll(".depoimento");
    const prevBtn = document.querySelector(".prev-depoimento");
    const nextBtn = document.querySelector(".next-depoimento");

    let index = 0;

    function showDepoimento(i) {
        if (i < 0) {
            index = depoimentos.length - 1;
        } else if (i >= depoimentos.length) {
            index = 0;
        } else {
            index = i;
        }

        carousel.style.transform = `translateX(${-index * 100}%)`;
    }

    prevBtn.addEventListener("click", () => {
        showDepoimento(index - 1);
    });

    nextBtn.addEventListener("click", () => {
        showDepoimento(index + 1);
    });

    // Auto-slide a cada 5 segundos
    setInterval(() => {
        showDepoimento(index + 1);
    }, 5000);
});


document.addEventListener("DOMContentLoaded", function () {
    const contatoForm = document.getElementById("contato-form");

    contatoForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const nome = contatoForm.nome.value.trim();
        const email = contatoForm.email.value.trim();
        const mensagem = contatoForm.mensagem.value.trim();

        if (nome === "" || email === "" || mensagem === "") {
            alert("Por favor, preencha todos os campos.");
            return;
        }

        alert("Mensagem enviada com sucesso! Retornaremos em breve.");
        contatoForm.reset();
    });

    // Efeito de entrada ao rolar a página
    const contatoSection = document.querySelector("#contato");

    function checkScroll() {
        const position = contatoSection.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            contatoSection.classList.add("visible");
        }
    }

    window.addEventListener("scroll", checkScroll);
});


document.addEventListener("DOMContentLoaded", function () {
    const botaoTopo = document.getElementById("voltar-topo");

    botaoTopo.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            botaoTopo.style.display = "block";
        } else {
            botaoTopo.style.display = "none";
        }
    });
});
