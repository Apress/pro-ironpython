using System;
using System.Text;

namespace IPEngine
{
    public class TestPlugin : BasePlugin
    {
        private EngineManager em;

        public override void ConfigurePlugin(string _displayName, string _className, string _methodName, string _fileLocation)
        {
            try
            {
                // set up the plugin properties
                SetPluginID();
                SetDisplayName(_displayName);
                SetClassName(_className);
                SetMethodName(_methodName);
                SetFileLocation(_fileLocation);
                SetStatus(pluginStatus.Loaded);

                // set up the instance of the plugin engine
                em = new EngineManager();
                em.Initialize(fileLocation);    
            }
            catch(Exception ex)
            {
                var error = ex.Message;
                SetStatus(pluginStatus.Failed);
            }
        }

        public override ExecuteResults ExecutePlugin<ExecuteResults>()
        {
            switch (status)
            {
                case pluginStatus.Loaded:
                    return em.Execute<ExecuteResults>(this);

                case pluginStatus.Failed:
                    throw new Exception("EngineManager failed to initialize plugin.");

                case pluginStatus.Unavailable:
                    throw new Exception("Plugin is unavailable; please initialize properly.");

                default:
                    throw new Exception("Unable to verify plugin status; please initialize properly.");
            }
        }

        public override ExecuteResults ExecutePlugin<ExecuteResults>(string[] parameters)
        {
            switch (status)
            {
                case pluginStatus.Loaded:
                    return em.Execute<ExecuteResults>(this, parameters);

                case pluginStatus.Failed:
                    throw new Exception("EngineManager failed to initialize plugin.");

                case pluginStatus.Unavailable:
                    throw new Exception("Plugin is unavailable; please initialize properly.");

                default:
                    throw new Exception("Unable to verify plugin status; please initialize properly.");
            }
        }

        public override string ToString()
        {
            var s = new StringBuilder();
            s.Append(displayName);
            s.Append(": ");
            s.Append(className);
            s.Append(" calling method ");
            s.Append(methodName);
            return s.ToString();
        }
    }
}
