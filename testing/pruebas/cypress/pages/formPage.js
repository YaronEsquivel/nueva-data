class formPage {
  elements = {
    userNameinput: () => cy.get(":nth-child(1) > td > input"),
    passwordInput: () => cy.get(":nth-child(2) > td > input"),
    currentAddressInput: () => cy.get("textarea"),
    filePicture: () => cy.get('[type="file"]'),
    checkbox1: () => cy.get("[value='cb1']"),
    checkbox2: () => cy.get("[value='cb2']"),
    checkbox3: () => cy.get("[value='cb3']"),

    genderMale: () => cy.get("[value='rd1']"),
    genderFemale: () => cy.get("[value='rd2']"),
    genderOther: () => cy.get("[value='rd3']"),

    contentItems: () => cy.get(":nth-child(7) > td"),
    selectionItem1: () => cy.get("[value='ms1']"),
    selectionItem2: () => cy.get("[value='ms2']"),
    selectionItem3: () => cy.get("[value='ms3']"),
    selectionItem4: () => cy.get("[value='ms4']"),

    selectDropDown: () => cy.get(":nth-child(8) > td > select"),
    dropDown01: () => cy.get(":nth-child(8) > td > select > [value='dd2']"),
    submitButton: () => cy.get("[type='submit']"),

    emailInput: () => cy.get("#userEmail"),
    numberInput: () => cy.get("#userNumber"),
    subjectInput: () => cy.get(".subjects-auto-complete__value-container"),

    dateOfBirth: () => cy.get("#dateOfBirthInput"),
    yearDate: () => cy.get(".react-datepicker__year-select"),
    monthDate: () => cy.get(".react-datepicker__month-select"),
    dayDate: () => cy.get(":nth-child(1) > .react-datepicker__day--002"),

    //123

    selectForm: () => cy.get("#htmlformtest"),
    confirmForm: () =>
      cy.get(":nth-child(2) > .element-list > .menu-list > #item-0"),
  };

  clickForm() {
    this.elements.selectForm().click();
    //this.elements.confirmForm().click();
  }

  typeUserNameInput(username) {
    this.elements.userNameinput().type(username);
  }

  typePassword(password) {
    this.elements.passwordInput().type(password);
  }

  typeCurrentAddress(currentAddressInput) {
    this.elements
      .currentAddressInput()
      .click()
      .clear()
      .type(currentAddressInput);
  }

  selectPicture(filePicture) {
    this.elements.filePicture().selectFile(filePicture);
  }

  typeEmail(email) {
    this.elements.emailInput().type(email);
  }

  selectGender(opcion) {
    if (opcion == "radio 1") {
      this.elements.genderMale().click();
    } else if (opcion == "radio 2") {
      this.elements.genderFemale().click();
    } else if (opcion == "radio 3") {
      this.elements.genderOther().click();
    }
  }
  selectItems(items) {
    let item = items.split("and" || ",")
    cy.log(item[0])
    cy.log(item[1])
    this.elements.contentItems().click();
    cy.wait(100);
    this.elements.selectionItem1().dblclick();

    /*
    
    this.elements.contentItems().click().select(item[0]);
    */
  }

  selectItemDropDown(dropDown01){
    this.elements.selectDropDown().select(dropDown01);
  }

  clickSubmitForm(){
    this.elements.submitButton().click();
  }

  typeNumber(number) {
    this.elements.numberInput().type(number);
  }

  selectDateOfBirth(date) {
    let fecha = date.split(" ");
    cy.log(fecha[0]);
    cy.log(fecha[1]);
    cy.log(fecha[2]);
    this.elements.dateOfBirth().click();
    this.elements.monthDate().select(fecha[1]);
    this.elements.yearDate().select(fecha[2]);
    this.elements.dateOfBirth().click();
    this.elements.dayDate().click();
  }

  typeSubject(subject) {
    this.elements.subjectInput().type(subject);
  }

  selectHobbie(checkbox) {
    switch (checkbox) {
      case "Checkbox 1":
        this.elements.checkbox1().click();
        this.elements.checkbox3().click();
        break;
      case "Checkbox 2":
        this.elements.checkbox2().click();
        this.elements.checkbox3().click();
        break;
      case "Checkbox 3":
        break;
      case "Checkbox 1 and Checkbox 2" || "Checkbox 2 and Checkbox 1":
        this.elements.checkbox2().click();
        this.elements.checkbox1().click();
        this.elements.checkbox3().click();
        break;
      case "Checkbox 1 and Checkbox 3" || "Checkbox 3 and Checkbox 1":
        this.elements.checkbox1().click();
        break;
      case "Checkbox 3 and Checkbox 2" || "Checkbox 2 and Checkbox 3":
        this.elements.checkbox2().click();
        break;
      case "Checkbox 1, Checkbox 2 and Checkbox 3" ||
        "Checkbox 1, Checkbox 3 and Checkbox 3" ||
        "Checkbox 2, Checkbox 1 and Checkbox 3" ||
        "Checkbox 2, Checkbox 3 and Checkbox 1" ||
        "Checkbox 3, Checkbox 2 and Checkbox 1" ||
        "Checkbox 3, Checkbox 1 and Checkbox 2":
        this.elements.checkbox1().click();
        this.elements.checkbox2().click();
        this.elements.checkbox3().click().wait(100).click();
        break;
      default:
        break;
    }
  } 
}

module.exports = new formPage();

/*
 switch (hobbie) {
      case "Sport":
        this.elements.hobbieSport().click();
        break;
      case "Reading":
        this.elements.hobbieReading().click();
        break;
      case "Music":
        this.elements.hobbieMusic().click();
        break;
      case "Sport and Reading" || "Reading and Sport":
        this.elements.hobbieSport().click();
        this.elements.hobbieReading().click();
        break;
      case "Sport and Music" || "Music and Sport":
        this.elements.hobbieSport().click();
        this.elements.hobbieMusic().click();
        break;
      case "Music and Reading" || "Reading and Music":
        this.elements.hobbieMusic().click();
        this.elements.hobbieReading().click();
        break;
      case 'Sport, Reading and Music"' || 'Music, Reading and Sport' || 'Sport, Music and Reading' 
        || 'Music, Sport and Reading' || 'Reading, Music and Sport' || 'Reading, Sport and Music':
        this.elements.hobbieSport().click();
        this.elements.hobbieMusic().click();
        this.elements.hobbieReading().click();
        break;
      default:
        break;
    }
*/
