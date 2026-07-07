#include<iostream>
#include<Windows.h>
#include<vector>
#include<string>
using namespace std;

class Contact {
private:
    string fullName;
    string homePhone;
    string workPhone;
    string email;
    string info;
public:
    Contact(string n, string h, string w, string e, string i) 
        : fullName(n), homePhone(h), workPhone(w), email(e), info(i) {}
    
    string getName() const { return fullName; }
    string getHomePhone() const { return homePhone; }
    string getWorkPhone() const { return workPhone; }
    string getEmail() const { return email; }
    string getInfo() const { return info; }
    
    void setName(string n) { fullName = n; }
    void setHomePhone(string h) { homePhone = h; }
    void setWorkPhone(string w) { workPhone = w; }
    void setEmail(string e) { email = e; }
    void setInfo(string i) { info = i; }
};

class PhoneDirectory {
private:
    vector<Contact> contacts;
public:
    void addContact(string fullName, string homePhone, string workPhone, string email, string info) {
        contacts.push_back(Contact(fullName, homePhone, workPhone, email, info));
    }
    
    bool removeContact(string fullName) {
        for (auto it = contacts.begin(); it != contacts.end(); ++it) {
            if (it->getName() == fullName) {
                contacts.erase(it);
                return true;
            }
        }
        return false;
    }
    
    Contact* findContact(string fullName) {
        for (auto& contact : contacts) {
            if (contact.getName() == fullName) {
                return &contact;
            }
        }
        return nullptr;
    }
    
    void displayAll() const {
        if (contacts.empty()) {
            cout << "Довідник порожній.\n";
            return;
        }
        cout << "\nСписок контактів:\n";
        for (const auto& contact : contacts) {
            cout << "ПІБ: " << contact.getName() << "\n"
                 << " Домашній: " << contact.getHomePhone() << "\n"
                 << " Робочий: " << contact.getWorkPhone() << "\n"
                 << " Email: " << contact.getEmail() << "\n"
                 << " Інфо: " << contact.getInfo() << "\n\n";
        }
    }
    
    bool isEmpty() const { return contacts.empty(); }
};

void showMenu() {
    cout << "\n=== Телефонний довідник ===\n";
    cout << "1. Додати контакт\n";
    cout << "2. Видалити контакт\n";
    cout << "3. Знайти контакт\n";
    cout << "4. Показати всі контакти\n";
    cout << "5. Вихід\n";
    cout << "Оберіть дію: ";
}

int main() {
    SetConsoleOutputCP(65001);
    SetConsoleCP(65001);
    
    PhoneDirectory directory;
    int choice;
    string fullName, homePhone, workPhone, email, info;
    
    do {
        showMenu();
        cin >> choice;
        cin.ignore();
        
        switch (choice) {
        case 1:
            cout << "Введіть ПІБ: ";
            getline(cin, fullName);
            cout << "Введіть домашній телефон: ";
            getline(cin, homePhone);
            cout << "Введіть робочий телефон: ";
            getline(cin, workPhone);
            cout << "Введіть email: ";
            getline(cin, email);
            cout << "Введіть інформацію: ";
            getline(cin, info);
            directory.addContact(fullName, homePhone, workPhone, email, info);
            cout << "Контакт доданий!\n";
            break;
        case 2:
            cout << "Введіть ПІБ для видалення: ";
            getline(cin, fullName);
            if (directory.removeContact(fullName))
                cout << "Контакт видалений!\n";
            else
                cout << "Контакт не знайдений!\n";
            break;
        case 3:
            cout << "Введіть ПІБ для пошуку: ";
            getline(cin, fullName);
            {
                Contact* contact = directory.findContact(fullName);
                if (contact) {
                    cout << "Домашній: " << contact->getHomePhone() << "\n"
                         << "Робочий: " << contact->getWorkPhone() << "\n"
                         << "Email: " << contact->getEmail() << "\n"
                         << "Інфо: " << contact->getInfo() << "\n";
                } else
                    cout << "Контакт не знайдений!\n";
            }
            break;
        case 4:
            directory.displayAll();
            break;
        case 5:
            cout << "До побачення!\n";
            break;
        default:
            cout << "Невірний вибір!\n";
        }
    } while (choice != 5);
    
    return 0;
}