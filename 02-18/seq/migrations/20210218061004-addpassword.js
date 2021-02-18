'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    //table이름 , 넣을 컬럼이름, 속성
    await queryInterface.addColumn("users", "password", {
      type:Sequelize.INTEGER
    })

  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.removeColumn("users", "password")
  }
};
