using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

namespace IPEngine
{
    public class EngineManager
    {
        private ScriptEngine engine;
        private ScriptSource source;
        private ScriptScope scope;
        private ObjectOperations operations;

        /// <summary>
        /// Sets up the IPEngine for use by calling code.
        /// </summary>
        /// <param name="file">The name of the IronPython source file to execute.</param>
        public void Initialize(string file)
        {
            engine = Python.CreateEngine();
            source = engine.CreateScriptSourceFromFile(file);
            scope = engine.CreateScope();
            operations = engine.Operations;
        }

        /// <summary>
        /// Gets the results of an IronPython file after execution.
        /// </summary>
        /// <typeparam name="EngineResults">Generic result from IronPython class.</typeparam>
        /// <param name="className">The name of the class to reference.</param>
        /// <param name="methodName">The name of the method to execute.</param>
        /// <returns>The results of IronPython execution.</returns>
        public EngineResults Execute<EngineResults>(string className, string methodName)
        {
            source.Execute(scope);
            var classObj = scope.GetVariable(className);
            var classInstance = operations.Call(classObj);
            var classMethod = operations.GetMember(classInstance, methodName);
            var results = (EngineResults) operations.Call(classMethod);
            return results;
        }

        /// <summary>
        /// Gets the results of an IronPython plugin after execution.
        /// </summary>
        /// <typeparam name="EngineResults">Generic result from IronPython class.</typeparam>
        /// <param name="plugin">A plugin that implements BasePlugin.</param>
        /// <returns>The results of IronPython execution.</returns>
        public EngineResults Execute<EngineResults>(BasePlugin plugin)
        {
            source.Execute(scope);
            var classObj = scope.GetVariable(plugin.className);
            var classInstance = operations.Call(classObj);
            var classMethod = operations.GetMember(classInstance, plugin.methodName);
            var results = (EngineResults)operations.Call(classMethod);
            return results;
        }

        /// <summary>
        /// Gets the results of an IronPython plugin after execution.
        /// </summary>
        /// <typeparam name="EngineResults">Generic result from IronPython class.</typeparam>
        /// <param name="plugin">A plugin that implements BasePlugin.</param>
        /// <param name="parameters">An array of string parameters.</param>
        /// <returns>The results of IronPython execution.</returns>
        public EngineResults Execute<EngineResults>(BasePlugin plugin, string[] parameters)
        {
            source.Execute(scope);
            var classObj = scope.GetVariable(plugin.className);
            var classInstance = operations.Call(classObj);
            var classMethod = operations.GetMember(classInstance, plugin.methodName);
            var results = (EngineResults)operations.Call(classMethod, parameters);
            return results;
        }
    }
}
