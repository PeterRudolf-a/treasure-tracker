fetch("http://localhost:5000/inventory/peter01")
  .then(res => res.json())
  .then(items => {
    const tbody = document.querySelector("tbody");
    items.forEach(([name, rarity, time]) => {
      const row = `<tr><td>${name}</td><td>${rarity}</td><td>${time}</td></tr>`;
      tbody.innerHTML += row;
    });
  });
