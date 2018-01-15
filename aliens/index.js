


// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $dateInput = document.querySelector("#datetime");
var $searchBtn = document.querySelector("#search");
var $loadMoreBtn = document.querySelector("#load-btn");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

var startingIndex = 0;
var resultsPerPage = 50;
// Set filterData to sightingData initially
var filterData = dataSet;

// renderTable renders the filterData to the tbody
// function renderTable() {
//   $tbody.innerHTML = "";
//   for (var i = 0; i < filterData.length; i++) {
//     // Get get the current sighting object and its fields
//     var sighting = filterData[i];
//     var fields = Object.keys(sighting);
//     // Create a new row in the tbody, set the index to be i + startingIndex
//     var $row = $tbody.insertRow(i);
//     for (var j = 0; j < fields.length; j++) {
//       // For every field in the sighting object, create a new cell at set its inner text to be the current value at the current sighting's field
//       var field = fields[j];
//       var $cell = $row.insertCell(j);
//       $cell.innerText = sighting[field];
//     }
//   }
// }

function renderTableSection() {
  // Set the value of endingIndex to startingIndex + resultsPerPage
  var endingIndex = startingIndex + resultsPerPage;
  // Get a section of the filterData array to render
  var sightingSubset = filterData.slice(startingIndex, endingIndex);
  for (var i = 0; i < sightingSubset.length; i++) {
    var sighting_ = sightingSubset[i];
    var fields = Object.keys(sighting_);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i + startingIndex);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell and set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting_[field];
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
  renderTableSection();
}

$loadMoreBtn.addEventListener("click", handleButtonClick);

function handleButtonClick() {
  // Increase startingIndex by 100 and render the next section of the table
  startingIndex += resultsPerPage;
  renderTableSection();
  // Check to see if there are any more results to render
  if (startingIndex + resultsPerPage >= filterData.length) {
    $loadMoreBtn.classList.add("disabled");
    $loadMoreBtn.innerText = "All Sightings Loaded";
    $loadMoreBtn.removeEventListener("click", handleButtonClick);
  }
}
// Render the table for the first time on page load
renderTableSection();
