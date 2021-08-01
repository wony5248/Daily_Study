const bcrypt = require('bcrypt');
const saltRounds = 10;

const hashPassword = async password => {
  try {
    const salt = await bcrypt.genSalt(saltRounds);
    const hashedPassword = await bcrypt.hash(password, salt);
    return hashedPassword;
  } catch (error) {
    console.log(error);
    return error;
  }
};

const comparedPassword = async (password, hashedPassword) => {
  try {
    return await bcrypt.compare(password, hashedPassword);
  } catch (error) {
    console.log(error);
    return error;
  }
};

module.exports = {
  hashPassword,
  comparedPassword
};