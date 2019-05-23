def p1(x, f, fL, fR, dx):
    return (23.57633877428808*fR[1]*x**5)/dx**5+(23.57633877428808*fL[1]*x**5)/dx**5+(81.44553394754065*f[1]*x**5)/dx**5-(18.56155300614687*fR[0]*x**5)/dx**5+(18.56155300614687*fL[0]*x**5)/dx**5+(2.296396633859228*fR[1]*x**4)/dx**4-(2.296396633859228*fL[1]*x**4)/dx**4-(1.325825214724776*fR[0]*x**4)/dx**4-(1.325825214724776*fL[0]*x**4)/dx**4+(2.651650429449552*f[0]*x**4)/dx**4-(12.5026038954558*fR[1]*x**3)/dx**3-(12.5026038954558*fL[1]*x**3)/dx**3-(45.41762231410475*f[1]*x**3)/dx**3+(10.16465997955662*fR[0]*x**3)/dx**3-(10.16465997955662*fL[0]*x**3)/dx**3-(1.913663861549357*fR[1]*x**2)/dx**2+(1.913663861549357*fL[1]*x**2)/dx**2+(1.458407736197253*fR[0]*x**2)/dx**2+(1.458407736197253*fL[0]*x**2)/dx**2-(2.916815472394507*f[0]*x**2)/dx**2+(1.243881510007081*fR[1]*x)/dx+(1.243881510007081*fL[1]*x)/dx+(7.08055628773262*f[1]*x)/dx-(1.027514541411701*fR[0]*x)/dx+(1.027514541411701*fL[0]*x)/dx+0.130767030539206*fR[1]-0.130767030539206*fL[1]-0.104961162832378*fR[0]-0.104961162832378*fL[0]+0.917029106851303*f[0]

def p1e(x, fL, fR, dx):
    return (3.061862178478972*fR[1]*x**3)/dx**3+(3.061862178478972*fL[1]*x**3)/dx**3-(1.767766952966368*fR[0]*x**3)/dx**3+(1.767766952966368*fL[0]*x**3)/dx**3+(1.224744871391589*fR[1]*x**2)/dx**2-(1.224744871391589*fL[1]*x**2)/dx**2-(1.530931089239486*fR[1]*x)/dx-(1.530931089239486*fL[1]*x)/dx+(1.590990257669731*fR[0]*x)/dx-(1.590990257669731*fL[0]*x)/dx-0.408248290463863*fR[1]+0.408248290463863*fL[1]+0.3535533905932737*fR[0]+0.3535533905932737*fL[0]

def p2(x, f, fL, fR, dx):
    return (-(105.4224314958633*fR[2]*x**6)/dx**6)-(105.4224314958633*fL[2]*x**6)/dx**6+(559.4859750252903*f[2]*x**6)/dx**6+(138.2430773583255*fR[1]*x**6)/dx**6-(138.2430773583255*fL[1]*x**6)/dx**6-(92.80776503073433*fR[0]*x**6)/dx**6-(92.80776503073433*fL[0]*x**6)/dx**6+(185.6155300614687*f[0]*x**6)/dx**6-(15.77185983008978*fR[2]*x**5)/dx**5+(15.77185983008978*fL[2]*x**5)/dx**5+(18.21807996194988*fR[1]*x**5)/dx**5+(18.21807996194988*fL[1]*x**5)/dx**5+(40.72276697377032*f[1]*x**5)/dx**5-(11.13693180368812*fR[0]*x**5)/dx**5+(11.13693180368812*fL[0]*x**5)/dx**5+(56.03160729110844*fR[2]*x**4)/dx**4+(56.03160729110844*fL[2]*x**4)/dx**4-(319.5876860307667*f[2]*x**4)/dx**4-(75.0156233727348*fR[1]*x**4)/dx**4+(75.0156233727348*fL[1]*x**4)/dx**4+(51.04427076690387*fR[0]*x**4)/dx**4+(51.04427076690387*fL[0]*x**4)/dx**4-(102.0885415338078*f[0]*x**4)/dx**4+(9.091548272984086*fR[2]*x**3)/dx**3-(9.091548272984086*fL[2]*x**3)/dx**3-(11.48198316929614*fR[1]*x**3)/dx**3-(11.48198316929614*fL[1]*x**3)/dx**3-(29.08769069555023*f[1]*x**3)/dx**3+(7.513009550107064*fR[0]*x**3)/dx**3-(7.513009550107064*fL[0]*x**3)/dx**3-(7.300414442029338*fR[2]*x**2)/dx**2-(7.300414442029338*fL[2]*x**2)/dx**2+(52.99285610204038*f[2]*x**2)/dx**2+(9.903210483517913*fR[1]*x**2)/dx**2-(9.903210483517913*fL[1]*x**2)/dx**2-(6.794854225464475*fR[0]*x**2)/dx**2-(6.794854225464475*fL[0]*x**2)/dx**2+(13.58970845092895*f[0]*x**2)/dx**2-(0.9412717097844931*fR[2]*x)/dx+(0.9412717097844931*fL[2]*x)/dx+(1.234313190699334*fR[1]*x)/dx+(1.234313190699334*fL[1]*x)/dx+(5.721854946032574*f[1]*x)/dx-(0.8286407592029846*fR[0]*x)/dx+(0.8286407592029846*fL[0]*x)/dx+0.1432907064763796*fR[2]+0.1432907064763796*fL[2]-1.670077889276424*f[2]-0.1961505458088089*fR[1]+0.1961505458088089*fL[1]+0.1353446573364875*fR[0]+0.1353446573364875*fL[0]+0.4364174665135718*f[0]

def p2e(x, fL, fR, dx):
    return (13.28156617270719*fR[2]*x**5)/dx**5-(13.28156617270719*fL[2]*x**5)/dx**5-(12.85982114961168*fR[1]*x**5)/dx**5-(12.85982114961168*fL[1]*x**5)/dx**5+(7.424621202458747*fR[0]*x**5)/dx**5-(7.424621202458747*fL[0]*x**5)/dx**5+(5.188111786213744*fR[2]*x**4)/dx**4+(5.188111786213744*fL[2]*x**4)/dx**4-(1.339564703084549*fR[1]*x**4)/dx**4+(1.339564703084549*fL[1]*x**4)/dx**4-(12.64911064067352*fR[2]*x**3)/dx**3+(12.64911064067352*fL[2]*x**3)/dx**3+(15.30931089239486*fR[1]*x**3)/dx**3+(15.30931089239486*fL[1]*x**3)/dx**3-(8.838834764831843*fR[0]*x**3)/dx**3+(8.838834764831843*fL[0]*x**3)/dx**3-(4.150489428970996*fR[2]*x**2)/dx**2-(4.150489428970996*fL[2]*x**2)/dx**2+(2.296396633859228*fR[1]*x**2)/dx**2-(2.296396633859228*fL[1]*x**2)/dx**2+(1.897366596101028*fR[2]*x)/dx-(1.897366596101028*fL[2]*x)/dx-(3.368048396326869*fR[1]*x)/dx-(3.368048396326869*fL[1]*x)/dx+(2.651650429449552*fR[0]*x)/dx-(2.651650429449552*fL[0]*x)/dx+0.3458741190809163*fR[2]+0.3458741190809163*fL[2]-0.4975526040028326*fR[1]+0.4975526040028326*fL[1]+0.3535533905932737*fR[0]+0.3535533905932737*fL[0]

recovCeFn = [p1, p2]
recovEdFn = [p1e, p2e]
