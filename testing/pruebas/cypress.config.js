const { defineConfig } = require("cypress");
const createBundler = require("@bahmutov/cypress-esbuild-preprocessor");
const addCucumberPreprocessorPlugin =
require("@badeball/cypress-cucumber-preprocessor").addCucumberPreprocessorPlugin;
const createEsbuildPlugin =
require("@badeball/cypress-cucumber-preprocessor/esbuild").createEsbuildPlugin;


module.exports = defineConfig({
  waitForAnimations: false,
  animationDistanceThreshold: 50,
  chromeWebSecurity: false,
  e2e: {
    specPattern: "cypress/e2e/features/*.feature",
    baseUrl: "https://testpages.herokuapp.com/styled/",
            
    async setupNodeEvents(on, config) {
      
      // implement node event listeners here
      const bundler = createBundler({
        plugins: [createEsbuildPlugin(config)],
      });
      on("file:preprocessor", bundler);
      await addCucumberPreprocessorPlugin(on, config);
        
      return config;
    },
  },
});