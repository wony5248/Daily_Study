'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert("order_lists", [
      {
        item: "chicken",
        type: "food",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        item: "pizza",
        type: "food",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        item: "hamburger",
        type: "food",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        item: "noodle",
        type: "food",
        createdAt: new Date(),
        updatedAt: new Date(),
      }
    ])
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete("order_lists", [])
  }
};
