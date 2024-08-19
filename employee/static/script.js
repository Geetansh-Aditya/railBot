// Function to create a complaint element
function createComplaintElement(complaint) {
    const complaintElement = document.createElement('div');
    complaintElement.classList.add('complaint');

    complaintElement.innerHTML = `
        <div class="info">
            <svg xmlns="http://www.w3.org/2000/svg" width="120px" height="120px" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="9" r="3" stroke="#1C274C" stroke-width="1.5"/>
                <path d="M17.9691 20C17.81 17.1085 16.9247 15 11.9999 15C7.07521 15 6.18991 17.1085 6.03076 20" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"/>
                <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
            <div class="text">
                <p>${complaint.client_name}</p>
                <p>Session Id: ${complaint.complaint_id}</p>
                <p>Complaint type: ${complaint.department}</p>
                <p>Complaint brief: ${complaint.complaint_brief}</p>
            </div>
        </div>
        <div class="actions">
            <span class="check">&#10004;</span>
            <span class="cross">&#10006;</span>
        </div>
    `;

    return complaintElement;
}

// Function to display all complaints
async function displayComplaints() {
    try {
        const response = await fetch('api/complaints/'); // Adjust URL if necessary
        if (!response.ok) {
            throw new Error('Failed to fetch complaints data');
        }
        const complaints = await response.json();

        const complaintsList = document.getElementById('complaints-list');

        // Clear existing complaints before appending new ones
        complaintsList.innerHTML = '';

        complaints.forEach(complaint => {
            const complaintElement = createComplaintElement(complaint);
            complaintsList.appendChild(complaintElement);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Initialize the display of complaints and set up periodic updates
document.addEventListener('DOMContentLoaded', () => {
    displayComplaints(); // Initial load
    setInterval(displayComplaints, 5000); // Fetch every 5 seconds
});
