//CHATBOT

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void displayFacilities() {
	cout << "\nCollege Facilities:" << endl;
	cout << "- Library with 24/7 access" << endl;
	cout << "- Hostel with comfortable rooms" << endl;
	cout << "- Sports Complex with various activities" << endl;
	cout << "- High-speed Wi-Fi Campus" << endl;
	cout << "- Cafeteria with delicious meals" << endl;
	cout << "\nWe ensure the best experience for our students!" << endl;
}

int displayCourses() {

	int ch;

	while(true) {
		cout << "\nAvailable Courses:" << endl;

		cout << "1.Computer Science Engineering" << endl;
		cout << "2.Mechanical Engineering" << endl;
		cout << "3.Electrical Engineering" << endl;
		cout << "4.Civil Engineering" << endl;
		cout << "5.AI & DS" << endl;
		cout << "6.Choose For Knowing Various Facilities of College" << endl;
		cout << "7.Exit" << endl;
		cout << "\nThese courses are designed to prepare you for a bright future!" <<endl;
		cout<<"Choose Course for knowing its fee structure or input any option for main menu"<<endl;
		cin>>ch;
		switch(ch) {
		case 1:
			cout << "CSE: Rs.96000/- Per Year." << endl;
			break;
		case 2:
			cout << "ME:Rs.90000/- Per Year" << endl;
			break;
		case 3:
			cout << "EE: Rs.95000/- Per Year" << endl;
			break;
		case 4:
			cout << "CE: Rs.85000/- Per Year" << endl;
			break;
		case 5:
			cout << "AI&DS: Rs.92000/- Per Year" << endl;
			break;

		case 6:

			displayFacilities();
			break;
		default:
		case 7:
			cout<<"Go to Main Menu"<<endl;
			return 0;
			break;
		}
	}

}

int main() {
	srand(time(0));
	string phone;
	int otp, inputOtp;

	cout << "\nWelcome to the College Enquiry Chatbot!" << endl;
	cout << "Please enter your phone number: ";
	cin >> phone;

	otp = rand() % 900 + 100;
	cout << "\nAn OTP has been sent to " << phone.substr(0, 3) << "" <<
	     phone.substr(7) << endl;
	cout << "OTP: " << otp << " (For testing, remove in real use)" << endl;

	while (true) {
		cout << "\nEnter OTP: ";
		cin >> inputOtp;
		if (inputOtp == otp) {
			cout << "OTP verified successfully!" << endl;
			break;
		} else {
			cout << "Incorrect OTP. Please try again." << endl;
		}
	}

	int choice;
	while (true) {
		cout << "\nHow can I assist you today?" << endl;
		cout << "1.View Available Courses" << endl;
		cout << "2.Check Fees Structure" << endl;
		cout << "3.Exit" << endl;
		cout << "\nEnter your choice: ";
		cin >> choice;

		switch (choice) {
		case 1:
			displayCourses();
			break;
		case 2:
			displayFacilities();

			break;
		case 3:
			cout << "\nThank you for using the College Enquiry Chatbot! Have a great day!" << endl;
			return 0;
		default:
			cout << "Invalid choice. Please try again." << endl;

		}
	}
}
