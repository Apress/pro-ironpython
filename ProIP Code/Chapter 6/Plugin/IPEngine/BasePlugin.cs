using System;

namespace IPEngine
{
    public abstract class BasePlugin
    {
        public enum pluginStatus
        {
            Unavailable,
            Loaded,
            Failed
        }

        public string id { get; private set; }
        public string displayName { get; private set; }
        public string className { get; private set; }
        public string methodName { get; private set; }
        public string fileLocation { get; private set; }
        public pluginStatus status { get; private set; }

        /// <summary>
        /// Initializes a unique ID for a plugin.
        /// </summary>
        public void SetPluginID()
        {
            if (!String.IsNullOrEmpty(id)) { throw new Exception("Plugin id has already been defined."); }
            id = Guid.NewGuid().ToString().ToLower();
        }

        /// <summary>
        /// Sets the friendly display name for a plugin.
        /// </summary>
        /// <param name="_displayName">The string to display.</param>
        public void SetDisplayName(string _displayName)
        {
            if (String.IsNullOrEmpty(_displayName)) { throw new Exception("Display name cannot be null."); }
            displayName = _displayName;
        }

        /// <summary>
        /// Sets the name of the IronPython class to use.
        /// </summary>
        /// <param name="_className">The name of the class.</param>
        public void SetClassName(string _className)
        {
            if (String.IsNullOrEmpty(_className)) { throw new Exception("Class name cannot be null."); }
            className = _className;
        }

        /// <summary>
        /// Sets the name of the IronPython method to execute.
        /// </summary>
        /// <param name="_methodName">The name of the method.</param>
        public void SetMethodName(string _methodName)
        {
            if (String.IsNullOrEmpty(_methodName)) { throw new Exception("Method name cannot be null."); }
            methodName = _methodName;
        }

        /// <summary>
        /// Sets the location of the plugin on disk.
        /// </summary>
        /// <param name="_fileLocation">The path of the file on disk.</param>
        public void SetFileLocation(string _fileLocation)
        {
            if (String.IsNullOrEmpty(_fileLocation)) { throw new Exception("File location cannot be null."); }
            fileLocation = _fileLocation;
        }

        /// <summary>
        /// Sets the current status of the plugin.
        /// </summary>
        /// <param name="_status">The status as defined by the pluginStatus enumeration.</param>
        public void SetStatus(pluginStatus _status)
        {
            if (status == _status) return;
            status = _status;
        }


        // classes that inherit from this base must implement the following methods
        public abstract void ConfigurePlugin(string _displayName, string _className, string _methodName,
                                             string _fileLocation);

        public abstract ExecuteResults ExecutePlugin<ExecuteResults>();
        public abstract ExecuteResults ExecutePlugin<ExecuteResults>(string[] parameters);
        public new abstract string ToString();
    }
}
