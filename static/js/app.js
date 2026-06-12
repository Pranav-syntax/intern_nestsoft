document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('a[href*="/delete/"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      if (!confirm("Are you sure you want to delete this car?")) {
        event.preventDefault();
      }
    });
  });
});
