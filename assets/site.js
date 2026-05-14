const lightbox = document.getElementById("lightbox");
const lightboxImage = lightbox?.querySelector(".lightbox-image");
const lightboxClose = lightbox?.querySelector(".lightbox-close");

function openLightbox(src, alt) {
  if (!lightbox || !lightboxImage) return;
  lightboxImage.src = src;
  lightboxImage.alt = alt;
  lightbox.hidden = false;
  document.body.classList.add("lightbox-open");
}

function closeLightbox() {
  if (!lightbox || !lightboxImage) return;
  lightbox.hidden = true;
  lightboxImage.src = "";
  lightboxImage.alt = "";
  document.body.classList.remove("lightbox-open");
}

document.querySelectorAll(".zoomable").forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault();
    openLightbox(link.dataset.lightboxSrc, link.dataset.lightboxAlt || "");
  });
});

lightboxClose?.addEventListener("click", closeLightbox);

lightbox?.addEventListener("click", (event) => {
  if (event.target === lightbox) closeLightbox();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closeLightbox();
});
