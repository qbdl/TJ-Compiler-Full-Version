module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? '/TJ_Compiler'
        : '/'
    ,
    productionSourceMap: false,
}
