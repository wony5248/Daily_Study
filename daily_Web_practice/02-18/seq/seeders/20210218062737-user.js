'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
   await queryInterface.bulkInsert("users", [
     {
       firstName: "jang",
       lastName: "beomjin",
       email: "wony5248@gmail.com",
       password: 1234,
       createdAt: new Date(),
       updatedAt: new Date(),
     }
   ])
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete("users", [])
  }
};
