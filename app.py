from flask import Flask, jsonify
import os
import logging
from security_utils import SecureLogger, secure_log_decorator, mask_secret
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

[SIS] [U3] [C5]

6 / 17
logger = logging.getLogger(__name__)
@app.route(&#39;/&#39;)
def home():
return jsonify({
&quot;message&quot;: &quot;Cofre Digital Online!&quot;,
&quot;environment&quot;: os.getenv(&#39;ENVIRONMENT&#39;, &#39;unknown&#39;),
&quot;version&quot;: os.getenv(&#39;APP_VERSION&#39;, &#39;1.0.0&#39;)
})
@app.route(&#39;/database&#39;)
def database_info():
db_host = os.getenv(&#39;DB_HOST&#39;, &#39;localhost&#39;)
db_user = os.getenv(&#39;DB_USER&#39;, &#39;user&#39;)
db_password = os.getenv(&#39;DB_PASSWORD&#39;, &#39;SENHA_NAO_CONFIGURADA&#39;)
logger.info(f&quot;Conectando ao banco: {db_host} com usuário: {db_user}&quot;)
return jsonify({
&quot;status&quot;: &quot;connected&quot; if db_password != &#39;SENHA_NAO_CONFIGURADA&#39; else
&quot;not_configured&quot;,
&quot;host&quot;: db_host,
&quot;user&quot;: db_user,
&quot;password_configured&quot;: db_password != &#39;SENHA_NAO_CONFIGURADA&#39;
})
@app.route(&#39;/api-key&#39;)
def api_key_info():
api_key = os.getenv(&#39;EXTERNAL_API_KEY&#39;, &#39;KEY_NAO_CONFIGURADA&#39;)
masked_key = mask_secret(api_key)
logger.info(f&quot;Usando API Key: {masked_key}&quot;)
return jsonify({
&quot;api_configured&quot;: api_key != &#39;KEY_NAO_CONFIGURADA&#39;,
&quot;key_preview&quot;: masked_key
})
if __name__ == &#39;__main__&#39;:
app.run(host=&#39;0.0.0.0&#39;, port=int(os.getenv(&#39;PORT&#39;, 5000)), debug=False)
