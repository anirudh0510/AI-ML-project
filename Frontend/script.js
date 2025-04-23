document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const fileInput = document.getElementById("videoInput");
    const file = fileInput.files[0];
    if (!file) {
      alert("Please upload a video first!");
      return;
    }

    const formData = new FormData();
    formData.append("video", file);

    const status = document.getElementById("status");
    status.innerText = "Analyzing video, please wait... ⚙️";

    try {
      const response = await fetch("/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Failed to process video");

      status.innerText =
        "✅ Analysis complete! Video is now showing in a new window.";
    } catch (err) {
      status.innerText = "❌ Error: " + err.message;
      console.error(err);
    }
  });
});
