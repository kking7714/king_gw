


// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $dateInput = document.querySelector("#datetime");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filterData to sightingData initially
var filterData = dataSet;

// renderTable renders the filterData to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filterData.length; i++) {
    // Get get the current sighting object and its fields
    var sighting = filterData[i];
    var fields = Object.keys(sighting);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the sighting object, create a new cell at set its inner text to be the current value at the current sighting's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDate = $dateInput.value.trim().toLowerCase();
  if (filterDate != "all"){
  // Set filterData to an array of all sightinges whose "state" matches the filter
    filterData = dataSet.filter(function(sighting) {
      var sightingDate = sighting.datetime.toLowerCase();

      // If true, add the sighting to the filterData, otherwise don't add it to filterData
      return sightingDate === filterDate;
    });}
  else {
    return sightingData;
  }
  renderTable();
}

// Render the table for the first time on page load
renderTable();
