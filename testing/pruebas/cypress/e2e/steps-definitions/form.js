import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

const formPage = require("../../pages/formPage");

Given("A web browser is at the demoqa page", () => {
  cy.visit("/");
  cy.screenshot('form-evidence1');
});

When("The user is select form", () => {
  formPage.clickForm();
  cy.screenshot('form-evidence2');
});

Then("A user enters the firstname {string}", (username) => {
  formPage.typeUserNameInput(username);
});

Then("A user enters the lastname {string}", (password) => {
  formPage.typePassword(password);
});

Then("The user enters his current address {string}", (currentAddress) => {
  formPage.typeCurrentAddress(currentAddress);
});

Then("The user select picture {string}",(picture)=>{
  formPage.selectPicture(picture);
})

Then("The user select his hobbies {string}", (hobbie) => {
  formPage.selectHobbie(hobbie);
})

Then("The user select his gender {string}", (gender) => {
  formPage.selectGender(gender);
});

Then("A user select multiple items {string}", (items) => {
  formPage.selectItems(items)
});

Then("A user select dropdown {string}", (dropdown) => {
  formPage.selectItemDropDown(dropdown)
});

Then("A user confirm form", () => {
  formPage.clickSubmitForm()
  cy.screenshot('form-evidence9');
});



//TODO --> UNUSED METHODS

Then("A user enters the email {string}", (email) => {
  formPage.typeEmail(email);
});


Then("the user select the date of birth {string}", (date) => {
  formPage.selectDateOfBirth(date);
})

Then("The user enters his cell phone number {string}", (number) => {
  formPage.typeNumber(number);
});

Then("The user enters his subject {string}", (subject) => {
  formPage.typeSubject(subject);
});
