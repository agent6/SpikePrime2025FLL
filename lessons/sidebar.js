// Sidebar and bottom navigation for Spike Prime FLL lessons

(function () {
  const LESSONS = [
    // Phase 1 – Python Basics
    { id: "lesson-01-python-foundations", title: "Lesson 1 – Python Foundations" },
    { id: "lesson-02-control-flow", title: "Lesson 2 – Control Flow" },
    { id: "lesson-03-loops-and-functions", title: "Lesson 3 – Loops and Functions" },
    { id: "lesson-04-lists-and-dicts", title: "Lesson 4 – Lists and Dictionaries" },

    // Phase 2 – Hardware & Runtime
    { id: "lesson-05-spike-hardware-and-ports", title: "Lesson 5 – Spike Hardware & Ports" },
    { id: "lesson-06-motors-encoders-motion-sensor", title: "Lesson 6 – Motors, Encoders, Motion Sensor" },
    { id: "lesson-07-async-and-runloop", title: "Lesson 7 – Async and runloop" },
    { id: "lesson-16-controlling-motion-with-tilt", title: "Lesson 16 – Controlling Motion with Tilt" },
    { id: "lesson-17-importing-libraries", title: "Lesson 17 – Importing Libraries" },
    { id: "lesson-18-making-moves-with-motors", title: "Lesson 18 – Making Moves with Motors" },
    { id: "lesson-19-start-sensing", title: "Lesson 19 – Start Sensing" },
    { id: "lesson-20-new-moves-with-motors", title: "Lesson 20 – New Moves with Motors" },

    // Phase 3 – Core Movement & Attachments
    { id: "lesson-08-straight-driving", title: "Lesson 8 – Straight Driving" },
    { id: "lesson-09-pivot-turns", title: "Lesson 9 – Pivot Turns" },
    { id: "lesson-10-spin-turns", title: "Lesson 10 – Spin Turns" },
    { id: "lesson-11-attachments", title: "Lesson 11 – Attachments" },
    { id: "lesson-12-async-motion-helpers", title: "Lesson 12 – Async Motion Helpers" },
    { id: "lesson-13-detecting-motor-stop", title: "Lesson 13 – Detecting Motor Stop" },
    { id: "lesson-14-mission-selector-ux", title: "Lesson 14 – Mission Selector UX" },
    { id: "lesson-15-mission-functions", title: "Lesson 15 – Mission Functions" },

    // Per-helper: Driving & Turning
    { id: "lesson-df-drive-forward", title: "Lesson DF – drive_forward" },
    { id: "lesson-db-drive-backward", title: "Lesson DB – drive_backward" },
    { id: "lesson-plo-pivot-left-outside", title: "Lesson PLO – pivot_left_outside" },
    { id: "lesson-pli-pivot-left-inside", title: "Lesson PLI – pivot_left_inside" },
    { id: "lesson-pro-pivot-right-outside", title: "Lesson PRO – pivot_right_outside" },
    { id: "lesson-pri-pivot-right-inside", title: "Lesson PRI – pivot_right_inside" },
    { id: "lesson-sl-spin-left", title: "Lesson SL – spin_left" },
    { id: "lesson-sr-spin-right", title: "Lesson SR – spin_right" },

    // Per-helper: Attachments
    { id: "lesson-lau-left-attachment-up", title: "Lesson LAU – left_attachment_up" },
    { id: "lesson-lad-left-attachment-down", title: "Lesson LAD – left_attachment_down" },
    { id: "lesson-rau-right-attachment-up", title: "Lesson RAU – right_attachment_up" },
    { id: "lesson-rad-right-attachment-down", title: "Lesson RAD – right_attachment_down" },

    // Per-helper: Async
    { id: "lesson-adf-async-drive-forward", title: "Lesson ADF – async_drive_forward" },
    { id: "lesson-adb-async-drive-backward", title: "Lesson ADB – async_drive_backward" },
    { id: "lesson-alau-async-left-attachment-up", title: "Lesson ALAU – async_left_attachment_up" },
    { id: "lesson-alad-async-left-attachment-down", title: "Lesson ALAD – async_left_attachment_down" },
    { id: "lesson-arau-async-right-attachment-up", title: "Lesson ARAU – async_right_attachment_up" },
    { id: "lesson-arad-async-right-attachment-down", title: "Lesson ARAD – async_right_attachment_down" },

    // Control helpers & missions
    { id: "lesson-mis-motor-is-stopped", title: "Lesson MIS – MotorIsStopped" },
    { id: "lesson-sel-mission-selector", title: "Lesson SEL – mission_selector" },
    { id: "lesson-mx-mission-0-9", title: "Lesson Mx – mission_0–mission_9" },
  ];

  const path = window.location.pathname;
  const file = path.split("/").pop();

  // Skip sidebar on index.html
  if (!file || file === "index.html") {
    return;
  }

  const currentBase = file.replace(/\.html$/, "");
  const currentIndex = LESSONS.findIndex((l) => `${l.id}` === currentBase);

  // Build the shell layout: sidebar + content wrapper
  const body = document.body;
  const originalChildren = Array.from(body.childNodes);
  body.innerHTML = "";

  const page = document.createElement("div");
  page.className = "page";

  const sidebar = document.createElement("aside");
  sidebar.className = "sidebar";

  const sidebarHeader = document.createElement("h2");
  sidebarHeader.textContent = "Lessons";
  sidebar.appendChild(sidebarHeader);

  const nav = document.createElement("nav");
  const list = document.createElement("ul");

  LESSONS.forEach((lesson, index) => {
    const li = document.createElement("li");
    if (index === currentIndex) {
      li.classList.add("current");
    }
    const a = document.createElement("a");
    a.href = `${lesson.id}.html`;
    a.textContent = lesson.title;
    li.appendChild(a);
    list.appendChild(li);
  });

  nav.appendChild(list);
  sidebar.appendChild(nav);

  const footer = document.createElement("div");
  footer.className = "sidebar-footer";
  footer.innerHTML =
    'Back to <a href="index.html">Lessons Index</a><br />' +
    '<a href="https://github.com/agent6/SpikePrime2025FLL" target="_blank" rel="noopener">View on GitHub</a>';
  sidebar.appendChild(footer);

  const toggle = document.createElement("button");
  toggle.className = "sidebar-toggle";
  toggle.textContent = "Lessons";
  toggle.addEventListener("click", () => {
    sidebar.classList.toggle("open");
  });

  const content = document.createElement("div");
  content.className = "content";
  const inner = document.createElement("div");
  inner.className = "content-inner";
  originalChildren.forEach((node) => inner.appendChild(node));
  content.appendChild(inner);

  page.appendChild(sidebar);
  page.appendChild(content);
  body.appendChild(toggle);
  body.appendChild(page);

  // Bottom navigation (prev / next / index)
  if (currentIndex !== -1) {
    const bottomNav = document.createElement("div");
    bottomNav.className = "bottom-nav";

    const prev = document.createElement("div");
    const next = document.createElement("div");
    const center = document.createElement("div");

    if (currentIndex > 0) {
      const prevLesson = LESSONS[currentIndex - 1];
      const aPrev = document.createElement("a");
      aPrev.href = `${prevLesson.id}.html`;
      aPrev.textContent = `← Previous: ${prevLesson.title}`;
      prev.appendChild(aPrev);
    } else {
      prev.textContent = "";
    }

    const indexLink = document.createElement("a");
    indexLink.href = "index.html";
    indexLink.textContent = "Back to Lessons Index";
    center.appendChild(indexLink);

    if (currentIndex < LESSONS.length - 1) {
      const nextLesson = LESSONS[currentIndex + 1];
      const aNext = document.createElement("a");
      aNext.href = `${nextLesson.id}.html`;
      aNext.textContent = `Next: ${nextLesson.title} →`;
      next.appendChild(aNext);
    } else {
      next.textContent = "";
    }

    bottomNav.appendChild(prev);
    bottomNav.appendChild(center);
    bottomNav.appendChild(next);
    inner.appendChild(bottomNav);
  }
})();
