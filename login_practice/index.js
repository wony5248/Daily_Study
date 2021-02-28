const express = require('express');
const app = express();
const PORT = 8000;
const db = require('./models');
const {
  hashPassword,
  comparedPassword
} = require('./utils/bcrypt');
const cookieParser = require('cookie-parser');

app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({
  extended: false
}));
app.set('view engine', 'ejs');

const authentication = async (req, res, next) => {
  if (req.cookies['loginId']) {
    try {
      const userInformation = await db['user'].findOne({
        where: {
          id: req.cookies['loginId'],
        },
      });
      //   Node 전역변수
      // 넘겨줘서 ejs에서도 사용가능하게끔
      res.locals.user = userInformation.dataValues;
    } catch (error) {
      res.locals.user = null;
    }
  }
  next();
};

app.use(authentication);

app.get('/', (req, res) => {
  return res.render('index');
});

app.get('/signup', (req, res) => {
  return res.render('signup')
})
app.get('/login', (req, res) => {
  return res.render('login')
})

app.post('/register', async (req, res) => {
  try {
    const {
      name,
      email,
      age,
      hobby,
      password
    } = req.body;

    const hashedPassword = await hashPassword(password);

    const data = await db['user'].create({
      name: name,
      email: email,
      hobby: hobby,
      age: age,
      password: hashedPassword
    })

    return res.render('logic', {
      type: 'register',
      result: true
    })
  } catch (error) {
    console.log(error);
    return res.render('logic', {
      type: 'register',
      result: false
    })
  }
})

app.post('/login', async (req, res) => {
  try {
    const {
      email,
      password
    } = req.body;

    const data = await db['user'].findOne({
      where: {
        email: email,
      }
    })

    const hashedPassword = data.password;
    const result = await comparedPassword(password, hashedPassword);

    if (result) {
      res.cookie('loginId', data.dataValues.id, {
        expires: new Date(Date.now() + 1000 * 60 * 60 * 24),
        httpOnly: true,
      })
      return res.render('logic', {
        type: 'login',
        result: true
      })
    } else {
      return res.render('logic', {
        type: 'login',
        result: false
      })
    }

  } catch (error) {
    console.log(error)
    return res.render('logic', {
      type: 'login',
      result: false
    })
  }
})

app.get('/logout', (req, res) => {
  res.clearCookie('loginId');
  res.locals.user = null;
  return res.redirect('/');
});

app.use(express.static('./static'));
app.listen(PORT, () => `this server is listening on ${PORT}`);