'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class order_list extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  order_list.init({
    item: DataTypes.STRING,
    type: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'order_list',
  });
  return order_list;
};