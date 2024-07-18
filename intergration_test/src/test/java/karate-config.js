function fn() {
  var env = karate.env; // get system property 'karate.env'
  karate.log('karate.env system property was:', env);
  if (!env) {
    env = 'dev';
  }
  // API url variable
  var config = {
    apiURL: 'http://127.0.0.1:8000/'
  }

  if (env == 'dev') {
    config.userEmail = 'aaa'
    config.userPassword = '1'

  } else if (env == 'qa') {
    config.userEmail ='nerdy@gmail.com'
    config.userPassword = '12345'
  }

  var accessSession = karate.callSingle('classpath:helpers/CreateCookies.feature', config).authsession
  console.log("kjkjhjk",accessSession)
  karate.configure('headers', {Cookie: "sessionid=" + accessSession })
  return config;
}